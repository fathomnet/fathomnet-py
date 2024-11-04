from enum import StrEnum
from typing import List
from typer import Typer

from fathomnet.api.darwincore import find_owner_institution_codes
from fathomnet.api.images import find_distinct_submitter, list_imaging_types
from fathomnet.api.taxa import list_taxa_providers


def create_typer_app() -> Typer:
    """
    Create the Typer app for the fathomnet-generate command.

    Returns:
        Typer: The Typer app for the fathomnet-generate command.
    """
    return Typer(
        name="fathomnet-generate",
        pretty_exceptions_short=True,
        pretty_exceptions_show_locals=False,
        help=__doc__,
        add_help_option=True,
        context_settings={"help_option_names": ["-h", "--help"]},
    )


def create_imaging_types_enum() -> StrEnum:
    """
    Create an enumeration of imaging types.

    Returns:
        StrEnum: The enumeration of imaging types.
    """
    imaging_type_strings = list_imaging_types()

    # Create a string enumerated class
    enum_cls = StrEnum(
        "ImagingTypes",
        {imaging_type.upper(): imaging_type for imaging_type in imaging_type_strings},
    )
    return enum_cls


def create_taxa_providers_enum() -> StrEnum:
    """
    Create an enumeration of taxa providers.

    Returns:
        StrEnum: The enumeration of taxa providers.
    """
    taxa_provider_strings = list_taxa_providers()

    # Create a string enumerated class
    enum_cls = StrEnum(
        "TaxaProviders",
        {
            taxa_provider.upper(): taxa_provider
            for taxa_provider in taxa_provider_strings
        },
    )
    return enum_cls


def get_contributor_emails() -> List[str]:
    """
    Get a list of valid contributor emails.

    Returns:
        List[str]: A list of valid contributor emails.
    """
    return find_distinct_submitter()


def get_owner_institution_codes() -> List[str]:
    """
    Get a list of valid owner institution codes.

    Returns:
        List[str]: A list of valid owner institution codes.
    """
    return find_owner_institution_codes()


class DatasetFormat(StrEnum):
    """
    Enumeration of available dataset output formats.
    """

    COCO = "COCO"
    VOC = "VOC"
    YOLO = "YOLO"


ImagingTypes = create_imaging_types_enum()

TaxaProviders = create_taxa_providers_enum()

VALID_CONTRIBUTOR_EMAILS = get_contributor_emails()

VALID_OWNER_INSTITUTION_CODES = get_owner_institution_codes()
