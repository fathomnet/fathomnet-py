"""
Model utility functions.
"""

from pathlib import Path
from typing import Optional
from urllib.parse import urlparse

from appdirs import user_cache_dir
from huggingface_hub import hf_hub_download
import requests


def get_cache_dir() -> Path:
    """
    Get the cache directory for the models.

    Returns:
        Path: The cache directory for the models.
    """
    return Path(user_cache_dir("fathomnet")) / "models"


def get_hf_file(repo_id: str, filename: str, revision: Optional[str] = None) -> Path:
    """
    Download/retrieve the file path for a file from Hugging Face.

    This function downloads a file from the Hugging Face Hub and saves it to the cache directory.
    If the file already exists in the cache directory, it will not be downloaded again.

    Args:
        repo_id (str): The repository ID of the model on the Hugging Face Hub.
        filename (str): The name of the file to download.
        revision (str, optional): The git revision to target. Defaults to "main".

    Returns:
        Path: The path to the downloaded file.
    """
    cache_dir = get_cache_dir() / "hf"
    cache_dir.mkdir(parents=True, exist_ok=True)

    # Download the file from Hugging Face Hub if it doesn't exist
    file_path = hf_hub_download(
        repo_id=repo_id, filename=filename, cache_dir=cache_dir, revision=revision
    )

    return Path(file_path)


def get_direct_file(model_id: str, url: str) -> Path:
    """
    Download/retrieve the file path for a file from the direct URL.

    This function downloads a file from a direct URL and saves it to the cache directory.
    If the file already exists in the cache directory, it will not be downloaded again.

    Args:
        model_id (str): The identifier for the model to disambiguate the file.
        url (str): The direct URL to download the file from.
    """
    parent_dir = get_cache_dir() / "direct" / model_id
    parent_dir.mkdir(parents=True, exist_ok=True)

    # Extract the file name from the URL
    parsed_url = urlparse(url)
    file_name = Path(parsed_url.path).name
    file_path = parent_dir / file_name

    # Download the file if it doesn't exist
    if not file_path.exists():
        with requests.get(url, stream=True) as r:
            r.raise_for_status()
            with file_path.open("wb") as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)

    return file_path
