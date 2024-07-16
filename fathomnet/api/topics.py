# topics.py (fathomnet-py)

from typing import List, Optional

from fathomnet import dto
from fathomnet.api import EndpointManager


class Topics(EndpointManager):
    PATH = "topics"


def create(
    topic: dto.Topic, auth_header: Optional[dto.AuthHeader] = None
) -> dto.FollowedTopic:
    """Follow a topic."""
    res_json = Topics.post("", json=topic.to_dict(), auth=auth_header)
    return dto.FollowedTopic.from_dict(res_json)


def find_by_uuid(
    uuid: str, auth_header: Optional[dto.AuthHeader] = None
) -> dto.FollowedTopic:
    """Get a followed topic by uuid."""
    res_json = Topics.get(uuid, auth=auth_header)
    return dto.FollowedTopic.from_dict(res_json)


def update(
    uuid: str, topic: dto.Topic, auth_header: Optional[dto.AuthHeader] = None
) -> dto.FollowedTopic:
    """Update a followed topic."""
    res_json = Topics.put(uuid, json=topic.to_dict(), auth=auth_header)
    return dto.FollowedTopic.from_dict(res_json)


def delete(
    uuid: str, auth_header: Optional[dto.AuthHeader] = None
) -> dto.FollowedTopic:
    """Unfollow a topic."""
    res_json = Topics.delete(uuid, auth=auth_header)
    return dto.FollowedTopic.from_dict(res_json)


def find(auth_header: Optional[dto.AuthHeader] = None) -> List[dto.FollowedTopic]:
    """Get a list of followed topics."""
    res_json = Topics.get("", auth=auth_header)
    return list(map(dto.FollowedTopic.from_dict, res_json))


def find_by_email(
    email: str, auth_header: Optional[dto.AuthHeader] = None
) -> List[dto.FollowedTopic]:
    """(Admin) Get a list of followed topics by email."""
    res_json = Topics.get("query/email/{}".format(email), auth=auth_header)
    return list(map(dto.FollowedTopic.from_dict, res_json))
