# darwincore.py (fathomnet-py)
import warnings
from typing import List

from fathomnet import dto
from fathomnet.api import EndpointManager


class DarwinCore(EndpointManager):
    PATH = "darwincore"


def index() -> str:
    """Get the darwin core index page.

    .. deprecated:: The FathomNet REST API no longer serves this endpoint.
    """
    warnings.warn(
        "darwincore.index() is deprecated: the endpoint was removed from the FathomNet REST API.",
        DeprecationWarning,
        stacklevel=2,
    )
    res = DarwinCore.get("", parse_json=False)
    return res.text


def find_owner_institution_codes() -> List[str]:
    """Get a list of owner institutions."""
    res_json = DarwinCore.get("list/ownerinstitutions")
    return res_json


def find_owner_institutions_by_image_uuid(image_uuid: str) -> List[str]:
    """Get a list of owner institutions by image UUID."""
    res_json = DarwinCore.get(f"query/ownerinstitutions/{image_uuid}")
    return res_json


def find_by_dataset_id(dataset_id: str) -> dto.BDarwinCore:
    """Get a darwin core record by its dataset ID (UUID)."""
    res_json = DarwinCore.get("query/datasetid/{}".format(dataset_id))
    return dto.BDarwinCore.from_dict(res_json)
