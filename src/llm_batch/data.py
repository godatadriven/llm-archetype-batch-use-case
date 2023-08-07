import logging
import os

logger = logging.getLogger(__name__)


def get_document_paths(folder_path: str) -> list[str]:
    if not os.path.isdir(folder_path):
        raise ValueError(f"'{folder_path}' is not a directory")

    paths = []
    for fname in os.listdir(folder_path):
        if os.path.isfile(fname):
            paths.append(folder_path + fname)
    return paths


def get_document_contents(document_paths: list[str]) -> dict[str]:
    ...
    return {"path": "content"}


def load_documents(folder_path: str) -> dict[str, str]:
    logger.info(f"Loading documents from '{folder_path}'")

    document_paths = get_document_paths(folder_path)
    documents = get_document_contents(document_paths)

    logger.info(f"Found {len(documents)} documents")
    return documents
