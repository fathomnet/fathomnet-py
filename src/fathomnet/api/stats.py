# stats.py (fathomnet-py)
from typing import List

from fathomnet import dto
from fathomnet.api import EndpointManager


class Stats(EndpointManager):
    PATH = "stats"


def most_popular_searches() -> List[str]:
    """Get a list of the most popular searches."""
    res_json = Stats.get("list/popular/searches")
    return res_json


def image_set_upload_positions() -> List[dto.ImageSetUploadPosition]:
    """Get a list of image set upload positions."""
    res_json = Stats.get("list/upload/positions")
    return [dto.ImageSetUploadPosition.from_dict(item) for item in res_json]


def contribution_stats() -> List[dto.ContributionStats]:
    """Get contribution stats by contributing institution."""
    res_json = Stats.get("list/contributions")
    return [dto.ContributionStats.from_dict(item) for item in res_json]
