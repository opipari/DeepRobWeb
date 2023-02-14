import os
import json
from typing import Any, Tuple

from PIL import Image

import torch
from torchvision import transforms
from torchvision.datasets.utils import check_integrity, download_and_extract_archive



class PROPSDetectionDataset(torch.utils.data.Dataset):

    base_folder = "PROPS-Detection-Dataset"
    url = "https://drive.google.com/file/d/1vG7_O-1JcYAgixdnV_n0QuFCt2R0050j/view?usp=share_link"
    filename = "PROPS-Detection-Dataset.tar.gz"
    tgz_md5 = "225d557f4980bd3e999d93411c3bebe6"

    object_list = [
        ["PROPS-Detection.tar.gz", "edb9252acb907894a478e8e1dc244da1"],
        ["train.json", "b4a5d081817e84ec9d47b30310172969"],
        ["val.json", "9ddab8ec4c2df411a982e00cf5430857"],
        ]


    def __init__(
        self, 
        root: str,
        split: str = "train",
        download: bool = False,
        image_size: int = 224,
        ) -> None:
        
        super().__init__()
        
        self.root = root
        self.split = split
        self.image_size = image_size
        self.dataset_dir = os.path.join(self.root, self.base_folder)
        
        if download:
            self.download()
            
        if not os.path.isdir(os.path.join(self.dataset_dir, "PROPS-Detection")):
            # Extract TAR file:
            import tarfile
    
            props_tar = tarfile.open(
                os.path.join(self.dataset_dir, "PROPS-Detection.tar.gz")
            )
            props_tar.extractall(self.dataset_dir)
            props_tar.close()
        

        if not self._check_integrity():
            raise RuntimeError("Dataset not found or corrupted. You can use download=True to download it")
        
        props_classes = [
            "master_chef_can", "cracker_box", "sugar_box",
            "tomato_soup_can", "mustard_bottle", "tuna_fish_can",
            "gelatin_box", "potted_meat_can", "mug", "large_marker"
        ]

        # Make a (class to ID) and inverse (ID to class) mapping.
        self.class_to_idx = {
            _class: _idx for _idx, _class in enumerate(props_classes)
        }
        self.idx_to_class = {
            _idx: _class for _idx, _class in enumerate(props_classes)
        }

        # Load instances from JSON file:
        self.instances = json.load(
            open(os.path.join(self.dataset_dir, f"{self.split}.json"))
        )
        
        # Define a transformation function for image: Resize the shorter image
        # edge then take a center crop (optional) and normalize.
        _transforms = [
            transforms.Resize(image_size),
            transforms.CenterCrop(image_size),
            transforms.ToTensor(),
            transforms.Normalize(
                mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]
            ),
        ]
        self.image_transform = transforms.Compose(_transforms)


    def __getitem__(self, index: int) -> Tuple[Any, Any]:
        # PIL image and dictionary of annotations.
        image_path, ann = self.instances[index]
        image_path = os.path.join(self.dataset_dir, image_path)
        image = Image.open(image_path).convert("RGB")

        # Collect a list of GT boxes: (N, 4), and GT classes: (N, )
        gt_boxes = torch.tensor([inst["xyxy"] for inst in ann])
        gt_classes = torch.Tensor([self.class_to_idx[inst["name"]] for inst in ann])
        gt_classes = gt_classes.unsqueeze(1)  # (N, 1)

        # Record original image size before transforming.
        original_width, original_height = image.size

        # Normalize bounding box co-ordinates to bring them in [0, 1]. This is
        # temporary, simply to ease the transformation logic.
        normalize_tens = torch.tensor(
            [original_width, original_height, original_width, original_height]
        )
        gt_boxes /= normalize_tens[None, :]

        # Transform input image to CHW tensor.
        image = self.image_transform(image)

        # WARN: Even dimensions should be even numbers else it messes up
        # upsampling in FPN.

        # Apply image resizing transformation to bounding boxes.
        if self.image_size is not None:
            if original_height >= original_width:
                new_width = self.image_size
                new_height = original_height * self.image_size / original_width
            else:
                new_height = self.image_size
                new_width = original_width * self.image_size / original_height

            _x1 = (new_width - self.image_size) // 2
            _y1 = (new_height - self.image_size) // 2

            # Un-normalize bounding box co-ordinates and shift due to center crop.
            # Clamp to (0, image size).
            gt_boxes[:, 0] = torch.clamp(gt_boxes[:, 0] * new_width - _x1, min=0)
            gt_boxes[:, 1] = torch.clamp(gt_boxes[:, 1] * new_height - _y1, min=0)
            gt_boxes[:, 2] = torch.clamp(
                gt_boxes[:, 2] * new_width - _x1, max=self.image_size
            )
            gt_boxes[:, 3] = torch.clamp(
                gt_boxes[:, 3] * new_height - _y1, max=self.image_size
            )

        # Concatenate GT classes with GT boxes; shape: (N, 5)
        gt_boxes = torch.cat([gt_boxes, gt_classes], dim=1)

        # Center cropping may completely exclude certain boxes that were close
        # to image boundaries. Set them to -1
        invalid = (gt_boxes[:, 0] > gt_boxes[:, 2]) | (
            gt_boxes[:, 1] > gt_boxes[:, 3]
        )
        gt_boxes[invalid] = -1

        # Pad to max 10 boxes, that's enough for PROPS.
        gt_boxes = torch.cat(
            [gt_boxes, torch.zeros(10 - len(gt_boxes), 5).fill_(-1.0)]
        )
        # Return image path because it is needed for evaluation.
        return image_path, image, gt_boxes


    def __len__(self) -> int:
        return len(self.instances)


    def _check_integrity(self) -> bool:
        for filename, md5 in self.object_list:
            fpath = os.path.join(self.root, self.base_folder, filename)
            if not check_integrity(fpath, md5):
                return False
        return True


    def download(self) -> None:
        if self._check_integrity():
            print("Files already downloaded and verified")
            return
        download_and_extract_archive(self.url, self.root, filename=self.filename, md5=self.tgz_md5)
