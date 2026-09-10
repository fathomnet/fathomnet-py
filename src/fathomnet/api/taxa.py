# taxa.py (fathomnet-py)
from typing import Iterator, List
from urllib.parse import quote

from fathomnet import dto
from fathomnet.api import EndpointManager, worms


class Taxa(EndpointManager):
    PATH = "taxa"


WORMS_PROVIDER_NAME = "worms"


def _is_worms(provider_name: str) -> bool:
    return provider_name.lower() == WORMS_PROVIDER_NAME


def _to_taxa(node: dto.WormsNode) -> dto.Taxa:
    """Narrow a WoRMS node to the name/rank pair the taxa endpoint returns."""
    return dto.Taxa(name=node.name, rank=node.rank)


def _walk(node: dto.WormsNode) -> Iterator[dto.WormsNode]:
    """Yield a WoRMS node and all of its descendants, depth-first."""
    yield node
    for child in node.children or []:
        yield from _walk(child)


def list_taxa_providers() -> List[str]:
    """Get a list of all taxa providers."""
    res_json = Taxa.get("list/providers")
    return res_json


def find_children(provider_name: str, concept: str) -> List[dto.Taxa]:
    """Find the taxonomic children for a concept according to a taxa provider."""
    if _is_worms(provider_name):
        return [_to_taxa(node) for node in worms.get_children(concept)]

    res_json = Taxa.get(
        "query/children/{}/{}".format(quote(provider_name), quote(concept))
    )
    return list(map(dto.Taxa.from_dict, res_json))


def find_parent(provider_name: str, concept: str) -> dto.Taxa:
    """Find the taxonomic parent for a concept according to a taxa provider."""
    if _is_worms(provider_name):
        return _to_taxa(worms.get_parent(concept))

    res_json = Taxa.get(
        "query/parent/{}/{}".format(quote(provider_name), quote(concept))
    )
    return dto.Taxa.from_dict(res_json)


def find_taxa(provider_name: str, concept: str) -> List[dto.Taxa]:
    """Get a list of all taxonomic descendants of a concept (including the concept itself) according to a taxa provider."""
    if _is_worms(provider_name):
        return [_to_taxa(node) for node in _walk(worms.get_descendants(concept))]

    res_json = Taxa.get("query/{}/{}".format(quote(provider_name), quote(concept)))
    return list(map(dto.Taxa.from_dict, res_json))
