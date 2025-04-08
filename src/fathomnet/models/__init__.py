# __init__.py (fathomnet-py)

try:
    import torch  # noqa: F401
except ImportError:
    raise ImportError(
        "You must install the 'models' extra to use the models subpackage: pip install fathomnet[models]"
    )

from fathomnet.models.registry import (
    MBARIMBBenthicModel,
    MBARIMidwaterSupercategory,
    MBARI315kYOLOv5,
    MBARI315kYOLOv8,
    Megalodon,
    VulnerableMarineEcosystems,
    TrashDetector,
    MegaFishDetector,
)

__all__ = [
    "MBARIMBBenthicModel",
    "MBARIMidwaterSupercategory",
    "MBARI315kYOLOv5",
    "MBARI315kYOLOv8",
    "Megalodon",
    "VulnerableMarineEcosystems",
    "TrashDetector",
    "MegaFishDetector",
]
