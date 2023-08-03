# stats.py (fathomnet-py)
from typing import List

from fathomnet.api import EndpointManager


class Stats(EndpointManager):
    PATH = 'stats'


def most_popular_searches() -> List[str]:
    """Get a list of the most popular searches."""
    res_json = Stats.get('list/popular/searches')
    return res_json
