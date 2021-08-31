# boundingboxes.py (fathomnet-py)
from typing import List, BinaryIO, Optional

from .. import models
from . import EndpointManager


class BoundingBoxes(EndpointManager):
    PATH = 'boundingboxes'


def create_with_dto(bounding_box: models.BBoundingBoxDTO, auth_header: Optional[models.AuthHeader] = None) -> models.BBoundingBoxDTO:
    """Create a bounding box."""
    res_json = BoundingBoxes.post('',
                                  json=bounding_box.to_dict(),
                                  auth=auth_header)
    return models.BBoundingBoxDTO.from_dict(res_json)


def count_all() -> models.Count:
    """Get a count of all bounding boxes."""
    res_json = BoundingBoxes.get('count')
    return models.Count.from_dict(res_json)


def find_concepts() -> List[str]:
    """Get a list of all concepts."""
    res_json = BoundingBoxes.get('list/concepts')
    return res_json


def count_total_by_concept() -> List[models.ByConceptCount]:
    """Get a count of bounding boxes for each concept."""
    res_json = BoundingBoxes.get('list/counts')
    return list(map(models.ByConceptCount.from_dict, res_json))


def find_observers() -> List[str]:
    """Get a list of all observers."""
    res_json = BoundingBoxes.get('list/observers')
    return res_json


def count_by_concept(concept: str) -> models.ByConceptCount:
    """Get a count of bounding boxes for a concept."""
    res_json = BoundingBoxes.get('query/count/{}'.format(concept))
    return models.ByConceptCount.from_dict(res_json)


def find_by_user_defined_key(user_defined_key: str) -> List[models.BBoundingBoxDTO]:
    """Get a list of bounding boxes by a user-defined key."""
    res_json = BoundingBoxes.get('query/userdefinedkey/{}'.format(user_defined_key))
    return list(map(models.BBoundingBoxDTO.from_dict, res_json))


def find_all_user_defined_keys() -> List[str]:
    """Get a list of all user-defined keys."""
    res_json = BoundingBoxes.get('query/userdefinedkeys')
    return res_json


def upload_csv(csv_fp: BinaryIO, auth_header: Optional[models.AuthHeader] = None) -> models.Message:
    """Upload a CSV of bounding boxes."""
    res_json = BoundingBoxes.post('upload/csv',
                                  files={'csv': csv_fp},
                                  auth=auth_header)
    return models.Message.from_dict(res_json)


def find_by_uuid(uuid: str) -> models.BBoundingBoxDTO:
    """Get a bounding box by UUID."""
    res_json = BoundingBoxes.get(uuid)
    return models.BBoundingBoxDTO.from_dict(res_json)


def update(uuid: str, bounding_box: models.ABoundingBoxDTO, auth_header: Optional[models.AuthHeader] = None) -> models.BBoundingBoxDTO:
    """Update a bounding box."""
    res_json = BoundingBoxes.put(uuid,
                                 json=bounding_box.to_dict(),
                                 auth=auth_header)
    return models.BBoundingBoxDTO.from_dict(res_json)


def delete(uuid: str, auth_header: Optional[models.AuthHeader] = None):
    """Delete a bounding box."""
    BoundingBoxes.delete(uuid, auth=auth_header)
