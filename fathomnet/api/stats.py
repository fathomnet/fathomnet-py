# stats.py (fathomnet-py)
from typing import List

from .. import models
from . import EndpointManager


class Stats(EndpointManager):
    PATH = 'stats'


def most_popular_searches() -> List[str]:
    res_json = Stats.get('list/popular/searches')
    return res_json
