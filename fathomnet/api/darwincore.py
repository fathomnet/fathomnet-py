# darwincore.py (fathomnet-py)
from typing import List

from fathomnet.api import EndpointManager


class DarwinCore(EndpointManager):
    PATH = 'darwincore'


def index() -> str:
    """Get the darwin core index page."""
    res = DarwinCore.get('', parse_json=False)
    return res.text


def find_owner_institution_codes() -> List[str]:
    """Get a list of owner institutions."""
    res_json = DarwinCore.get('list/ownerinstitutions')
    return res_json
