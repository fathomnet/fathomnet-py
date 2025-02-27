from os import getenv
from typing import List

from fathomnet.api import EndpointManager
from fathomnet.dto import WormsNames, WormsNode

FATHOMNET_WORMS_API_URL_DEFAULT = "https://database.fathomnet.org/worms"


def get_worms_api_url() -> str:
    """
    Get the Fast WoRMS API URL from the `FATHOMNET_WORMS_API_URL` environment variable or use the default value.

    Returns:
        str: The Fast WoRMS API base URL.
    """
    return getenv("FATHOMNET_WORMS_API_URL", FATHOMNET_WORMS_API_URL_DEFAULT)


class Worms(EndpointManager):
    ROOT = get_worms_api_url()
    PATH = ""


def count_names() -> int:
    """Get the total number of names available."""
    return int(Worms.get("names/count"))


def get_all_names(limit: int = 100, offset: int = 0) -> List[str]:
    """Get all names."""
    res_json = Worms.get("names", params={"limit": limit, "offset": offset})
    return res_json["items"]


def get_names_by_aphia_id(aphia_id: int) -> WormsNames:
    """Get the names data for a given Aphia ID."""
    res_json = Worms.get(f"names/aphiaid/{aphia_id}")
    return WormsNames.from_dict(res_json)


def get_ancestors_names(name: str) -> List[str]:
    """Get all ancestors' names of a given name."""
    return Worms.get(f"ancestors/{name}")


def get_children_names(name: str) -> List[str]:
    """Get all children's names of a given name."""
    return Worms.get(f"children/{name}")


def get_descendants_names(name: str, accepted: bool = False) -> List[str]:
    """Get all descendants' names of a given name."""
    return Worms.get(f"descendants/{name}", params={"accepted": accepted})


def get_parent_name(name: str) -> str:
    """Get the parent's name of a given name."""
    return Worms.get(f"parent/{name}")


def find_names_containing(fragment: str) -> List[str]:
    """Get all names that contain a fragment."""
    return Worms.get(f"query/contains/{fragment}")


def find_names_by_prefix(prefix: str) -> List[str]:
    """Get all names that start with a prefix."""
    return Worms.get(f"query/startswith/{prefix}")


def get_synonyms_for_name(name: str) -> List[str]:
    """Get all synonyms for a name."""
    return Worms.get(f"synonyms/{name}")


def get_ancestors(name: str) -> WormsNode:
    """Get a taxa tree from the root node to the node for the given name."""
    res_json = Worms.get(f"taxa/ancestors/{name}")
    return WormsNode.from_dict(res_json)


def get_children(name: str) -> List[WormsNode]:
    """Get the child taxa nodes of a given name."""
    res_json = Worms.get(f"taxa/children/{name}")
    return [WormsNode.from_dict(item) for item in res_json]


def get_descendants(name: str) -> WormsNode:
    """Get a taxa tree from the given name to the leaves."""
    res_json = Worms.get(f"taxa/descendants/{name}")
    return WormsNode.from_dict(res_json)


def get_parent(name: str) -> WormsNode:
    """Get the parent taxa node of a given name."""
    res_json = Worms.get(f"taxa/parent/{name}")
    return WormsNode.from_dict(res_json)


def get_info(name: str) -> WormsNode:
    """Get a taxa node for a given name."""
    res_json = Worms.get(f"taxa/info/{name}")
    return WormsNode.from_dict(res_json)


def find_taxa_by_prefix(
    prefix: str, rank: str = None, parent: str = None
) -> List[WormsNode]:
    """Get all taxa nodes that start with a prefix."""
    params = {}
    if rank is not None:
        params["rank"] = rank
    if parent is not None:
        params["parent"] = parent

    res_json = Worms.get(f"taxa/query/startswith/{prefix}", params=params)
    return [WormsNode.from_dict(item) for item in res_json]
