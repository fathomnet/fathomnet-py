# taxa.py (fathomnet-py)
from typing import List

from .. import models
from . import EndpointManager


class Taxa(EndpointManager):
    PATH = 'taxa'


def index() -> str:
    res = Taxa.get('', parse_json=False)
    return res.text


def list_taxa_providers() -> List[str]:
    res_json = Taxa.get('list/providers')
    return res_json


def find_children(provider_name: str, concept: str) -> List[models.Taxa]:
    res_json = Taxa.get('query/children/{}/{}'.format(provider_name, concept))
    return list(map(models.Taxa.from_dict, res_json))


def find_parent(provider_name: str, concept: str) -> models.Taxa:
    res_json = Taxa.get('query/parent/{}/{}'.format(provider_name, concept))
    return models.Taxa.from_dict(res_json)


def find_taxa(provider_name: str, concept: str) -> List[models.Taxa]:
    res_json = Taxa.get('query/{}/{}'.format(provider_name, concept))
    return list(map(models.Taxa.from_dict, res_json))
