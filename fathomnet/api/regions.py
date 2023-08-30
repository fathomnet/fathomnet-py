# regions.py (fathomnet-py)
from typing import List, Optional

from fathomnet import dto
from fathomnet.api import EndpointManager


class Regions(EndpointManager):
    PATH = 'regions'


def find_all() -> List[dto.MarineRegion]:
    """Get a list of all marine regions."""
    res_json = Regions.get('')
    return list(map(dto.MarineRegion.from_dict, res_json))


def count_all() -> int:
    """Get a count of all marine regions."""
    res = Regions.get('count', parse_json=False)
    return int(res.content)


def find_all_paged(pageable: Optional[dto.Pageable]) -> List[dto.MarineRegion]:
    """Get a paged list of all marine regions."""
    res_json = Regions.get('list/all', params=pageable.to_params() if pageable else None)
    return list(map(dto.MarineRegion.from_dict, res_json.get('content', [])))


def sync(auth_header: Optional[dto.AuthHeader] = None) -> int:
    """Synchronize."""
    res = Regions.get('sync', parse_json=False, auth=auth_header)
    return int(res.content)


def find_at(latitude: float, longitude: float) -> List[dto.MarineRegion]:
    """Get the marine regions at the given latitude and longitude."""
    res_json = Regions.get('at', params={'latitude': latitude, 'longitude': longitude})
    return list(map(dto.MarineRegion.from_dict, res_json))
