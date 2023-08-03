# __init__.py (fathomnet-py)

try:
    import torch
except ImportError:
    raise ImportError("You must install the 'models' extra to use the models subpackage: pip install fathomnet[models]")

from fathomnet.models.yolov5 import MBARIMBBenthicModel
