# taxa.py (fathomnet-py)
from typing import List

from .. import models
from . import EndpointManager


class Taxa(EndpointManager):
    PATH = 'taxa'


def index() -> str:
    """Get the taxa index page."""
    res = Taxa.get('', parse_json=False)
    return res.text


def list_taxa_providers() -> List[str]:
    """Get a list of all taxa providers."""
    res_json = Taxa.get('list/providers')
    return res_json


def find_children(provider_name: str, concept: str) -> List[models.Taxa]:
    """Find the taxonomic children for a concept according to a taxa provider."""
    res_json = Taxa.get('query/children/{}/{}'.format(provider_name, concept))
    return list(map(models.Taxa.from_dict, res_json))


def find_parent(provider_name: str, concept: str) -> models.Taxa:
    """Find the taxonomic parent for a concept according to a taxa provider."""
    res_json = Taxa.get('query/parent/{}/{}'.format(provider_name, concept))
    return models.Taxa.from_dict(res_json)


def find_taxa(provider_name: str, concept: str) -> List[models.Taxa]:
    """Get a list of all taxonomic descendants of a concept (including the concept itself) according to a taxa provider."""
    res_json = Taxa.get('query/{}/{}'.format(provider_name, concept))
    return list(map(models.Taxa.from_dict, res_json))
