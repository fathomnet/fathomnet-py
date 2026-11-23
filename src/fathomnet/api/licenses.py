# licenses.py (fathomnet-py)
from typing import List
from urllib.parse import quote

from fathomnet import dto
from fathomnet.api import EndpointManager


class Licenses(EndpointManager):
    PATH = "licenses"


def find_all() -> List[dto.FullLicense]:
    """Get a list of all supported licenses."""
    res_json = Licenses.get("list/all")
    return list(map(dto.FullLicense.from_dict, res_json))


def find_by_spdx_id_or_url(spdx_id_or_url: str) -> dto.FullLicense:
    """Get a license by its SPDX identifier (e.g. ``CC-BY-4.0``) or URL."""
    res_json = Licenses.get("search/{}".format(quote(spdx_id_or_url, safe="")))
    return dto.FullLicense.from_dict(res_json)
