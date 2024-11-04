"""
Generate an object detection dataset from FathomNet localizations.
"""

from typer import Option, Argument  # noqa: F401

from fathomnet.scripts.fathomnet_generate import (  # noqa: F401
    create_typer_app,
    VALID_OWNER_INSTITUTION_CODES,
    VALID_CONTRIBUTOR_EMAILS,
    ImagingTypes,
    TaxaProviders,
    DatasetFormat,
)

# Create the Typer app
app = create_typer_app()


@app.command()
def main():
    pass


if __name__ == "__main__":
    # Run the Typer app
    app()
