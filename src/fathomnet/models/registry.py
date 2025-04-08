"""
Registry of FathomNet Models.
"""

from fathomnet.models.bases import ImageModel
from fathomnet.models.wrappers import YOLOv5Model, UltralyticsModel
from fathomnet.models.utils import get_hf_file, get_direct_file


def MBARIMBBenthicModel() -> ImageModel:
    """
    MBARI Monterey Bay Benthic Object Detector.
    """
    weights = get_direct_file(
        "MBARI-MB-benthic",
        "https://zenodo.org/record/5539915/files/mbari-mb-benthic-33k.pt",
    )
    return YOLOv5Model(weights)


def MBARIMidwaterSupercategory() -> ImageModel:
    """
    MBARI Midwater Supercategory Object Detector.
    """
    weights = get_hf_file(
        "FathomNet/MBARI-midwater-supercategory-detector",
        "best.pt",
    )
    return YOLOv5Model(weights)


def MBARI315kYOLOv5() -> ImageModel:
    """
    MBARI 315k YOLOv5 Object Detector.
    """
    weights = get_hf_file(
        "FathomNet/MBARI-315k-yolov5",
        "mbari_315k_yolov5.pt",
    )
    return YOLOv5Model(weights)


def MBARI315kYOLOv8() -> ImageModel:
    """
    MBARI 315k YOLOv8 Object Detector.
    """
    weights = get_hf_file(
        "FathomNet/MBARI-315k-yolov8",
        "mbari_315k_yolov8.pt",
    )
    return UltralyticsModel(weights)


def Megalodon() -> ImageModel:
    """
    Megalodon Object Detector.
    """
    weights = get_hf_file(
        "FathomNet/megalodon",
        "mbari-megalodon-yolov8x.pt",
    )
    return UltralyticsModel(weights)


def VulnerableMarineEcosystems() -> ImageModel:
    """
    Vulnerable Marine Ecosystems Object Detector.
    """
    weights = get_hf_file(
        "FathomNet/vulnerable-marine-ecosystems",
        "best.pt",
    )
    return UltralyticsModel(weights)


def TrashDetector() -> ImageModel:
    """
    Trash Detector.
    """
    weights = get_hf_file(
        "FathomNet/trash-detector",
        "trash_mbari_09072023_640imgsz_50epochs_yolov8.pt",
    )
    return UltralyticsModel(weights)


def MegaFishDetector(size: str = "m") -> ImageModel:
    """
    MegaFishDetector.

    Args:
        size (str): Size of the model. Options are "s", "m", "l". Default is "m".

    Raises:
        ValueError: If the size is not one of the specified options.
    """
    if size not in ("s", "m", "l"):
        raise ValueError("Invalid size. Options are 's', 'm', 'l'.")

    filename = {
        "l": "megafishdetector_v0_yolov5l_640p.pt",
        "m": "megafishdetector_v0_yolov5m_1280p.pt",
        "s": "megafishdetector_v0_yolov5s_640p.pt",
    }[size]

    weights = get_hf_file(
        "FathomNet/megafishdetector",
        f"weights/{filename}",
    )
    return YOLOv5Model(weights)
