from pathlib import Path
from typing import Iterable

import numpy as np
from torch.hub import load
from ultralytics import YOLO

from fathomnet.dto import BoundingBox
from fathomnet.models.bases import ImageModel


class YOLOv5Model(ImageModel):
    """
    YOLOv5 object detection model.
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


class UltralyticsModel(ImageModel):
    """
    Ultralytics object detection model.
    """

    def __init__(self, weights: Path) -> None:
        super().__init__()

        self._model = YOLO(weights)

    def _predict(self, image: np.ndarray) -> Iterable[BoundingBox]:
        detections = self._model.predict(image)

        for detection in detections[0].boxes.data:
            x1, y1, x2, y2, confidence, class_id = detection
            yield BoundingBox(
                concept=self._model.names[int(class_id)],
                x=int(x1),
                y=int(y1),
                width=int(x2 - x1),
                height=int(y2 - y1),
            )
