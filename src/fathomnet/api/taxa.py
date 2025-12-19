# taxa.py (fathomnet-py)
from typing import List
from urllib.parse import quote

from fathomnet import dto
from fathomnet.api import EndpointManager


class Taxa(EndpointManager):
    PATH = "taxa"


def list_taxa_providers() -> List[str]:
    """Get a list of all taxa providers."""
    res_json = Taxa.get("list/providers")
    return res_json


def find_children(provider_name: str, concept: str) -> List[dto.Taxa]:
    """Find the taxonomic children for a concept according to a taxa provider."""
    res_json = Taxa.get(
        "query/children/{}/{}".format(quote(provider_name), quote(concept))
    )
    return list(map(dto.Taxa.from_dict, res_json))


def find_parent(provider_name: str, concept: str) -> dto.Taxa:
    """Find the taxonomic parent for a concept according to a taxa provider."""
    res_json = Taxa.get(
        "query/parent/{}/{}".format(quote(provider_name), quote(concept))
    )
    return dto.Taxa.from_dict(res_json)


def find_taxa(provider_name: str, concept: str) -> List[dto.Taxa]:
    """Get a list of all taxonomic descendants of a concept (including the concept itself) according to a taxa provider."""
    res_json = Taxa.get("query/{}/{}".format(quote(provider_name), quote(concept)))
    return list(map(dto.Taxa.from_dict, res_json))
