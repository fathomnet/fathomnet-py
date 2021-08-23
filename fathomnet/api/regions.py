# regions.py (fathomnet-py)
from typing import List, Optional

from .. import models
from . import EndpointManager


class Regions(EndpointManager):
    PATH = 'regions'


def find_all() -> List[models.MarineRegion]:
    res_json = Regions.get('')
    return list(map(models.MarineRegion.from_dict, res_json))


def count_all() -> int:
    res = Regions.get('count', parse_json=False)
    return int(res.content)


def find_all_paged(pageable: models.Pageable) -> List[models.MarineRegion]:
    res_json = Regions.get('list/all',
                           params=pageable.to_params())
    return list(map(models.MarineRegion.from_dict, res_json['content']))


def sync(auth_header: Optional[models.AuthHeader] = None) -> int:
    res = Regions.get('sync', parse_json=False, auth=auth_header)
    return int(res.content)
