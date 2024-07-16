# geoimages.py (fathomnet-py)
from typing import List, Optional

from fathomnet import dto
from fathomnet.api import EndpointManager


class GeoImages(EndpointManager):
    PATH = "geoimages"


def find_all(pageable: Optional[dto.Pageable] = None) -> List[dto.GeoImage]:
    """Get a paged list of all geo images."""
    res_json = GeoImages.get("", params=pageable.to_params() if pageable else None)
    # Note: schema inconsistent with response, need to grab the 'content' object
    return list(map(dto.GeoImage.from_dict, res_json.get("content", [])))


def count(
    geo_image_constraints: dto.GeoImageConstraints,
) -> dto.GeoImageConstraintsCount:
    """Get a constrained count of geo images."""
    res_json = GeoImages.post("count", json=geo_image_constraints.to_dict())
    return dto.GeoImageConstraintsCount.from_dict(res_json)


def find(geo_image_constraints: dto.GeoImageConstraints) -> List[dto.GeoImage]:
    """Get a constrained list of geo images."""
    res_json = GeoImages.post("query", json=geo_image_constraints.to_dict())
    return list(map(dto.GeoImage.from_dict, res_json))


def find_by_image_set_upload_uuid(
    image_set_upload_uuid: str,
    limit: Optional[int] = None,
    offset: Optional[int] = None,
) -> List[dto.GeoImage]:
    """Get a list of geo images corresponding to an image set upload UUID."""
    res_json = GeoImages.get(
        "query/imagesetupload/{}".format(image_set_upload_uuid),
        params={"limit": limit, "offset": offset},
    )
    return list(map(dto.GeoImage.from_dict, res_json))
