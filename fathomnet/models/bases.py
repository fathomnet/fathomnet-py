# bases.py (fathomnet-py)

from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any, Iterable, TypeVar, Union

import cv2
import numpy as np

from fathomnet.dto import BoundingBox

T = TypeVar("T")


class ImageModel(ABC):
    """
    Abstract base class for image models. Defines the interface for models that can be used to predict on images.
    """
    @abstractmethod
    def _predict(self, image: Union[np.ndarray, Path]) -> T:
        raise NotImplementedError

    def predict(self, image: Union[np.ndarray, Path]) -> T:
        return self._predict(self._load(image))

    def _load(self, image: Union[np.ndarray, Path]) -> np.ndarray:
        if isinstance(image, Path):
            image = cv2.imread(str(image))
            return image

        return image
