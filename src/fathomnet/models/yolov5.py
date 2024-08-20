# yolov5.py (fathomnet-py)


from pathlib import Path
from typing import Iterable

import numpy as np
import requests
from appdirs import user_cache_dir
from torch.hub import load

from fathomnet.dto import BoundingBox
from fathomnet.models.bases import ImageModel


class YOLOv5Model(ImageModel):
    """
    YOLOv5 object detection model. Uses a .pt file and performs object detection on images.
    """

    def __init__(self, weights: Path) -> None:
        super().__init__()

        self._model = load("ultralytics/yolov5", "custom", path=weights)

    def _predict(self, image: np.ndarray) -> Iterable[BoundingBox]:
        detections = self._model(image)

        for detection in detections.xyxy[0]:
            x1, y1, x2, y2, confidence, class_id = detection
            yield BoundingBox(
                concept=self._model.names[int(class_id)],
                x=int(x1),
                y=int(y1),
                width=int(x2 - x1),
                height=int(y2 - y1),
            )


class MBARIMBBenthicModel(YOLOv5Model):
    """
    MBARI Monterey Bay Benthic Object Detector.
    """

    WEIGHTS_URL = "https://zenodo.org/record/5539915/files/mbari-mb-benthic-33k.pt"

    def __init__(self) -> None:
        cache_dir = Path(user_cache_dir("fathomnet"))
        mbari_mb_benthic_dir = cache_dir / "mbari-mb-benthic"
        weights = mbari_mb_benthic_dir / "mbari-mb-benthic-33k.pt"
        if not weights.exists():
            print(
                "Downloading MBARI Monterey Bay Benthic Object Detector weights to {}".format(
                    weights
                )
            )
            weights.parent.mkdir(parents=True, exist_ok=True)
            with requests.get(self.WEIGHTS_URL, stream=True) as r:
                r.raise_for_status()
                with weights.open("wb") as f:
                    for chunk in r.iter_content(chunk_size=8192):
                        f.write(chunk)

        super().__init__(weights)
