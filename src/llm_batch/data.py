import logging
import os
from pathlib import Path

import PyPDF2

logger = logging.getLogger(__name__)


def get_document_paths(folder_path: Path) -> list[Path]:
    if not os.path.isdir(folder_path):
        raise ValueError(f"'{folder_path}' is not a directory")

    paths = []
    for fname in os.listdir(folder_path):
        document_path = folder_path / fname
        if os.path.isfile(document_path):
            paths.append(document_path)
    return paths


def get_pdf_documents_content(document_paths: list[Path]) -> dict[Path, dict]:
    documents_content: dict[Path, dict] = {}
    for path in document_paths:
        documents_content[path] = {}
        with open(path, "rb") as f:
            pdf_reader = PyPDF2.PdfReader(f)
            content = ""
            for page_num in range(len(pdf_reader.pages)):
                content += pdf_reader.pages[page_num].extract_text()
            documents_content[path]["processed"] = content
    return documents_content


def get_txt_documents_content(document_paths: list[Path]) -> dict[Path, dict]:
    documents_content: dict[Path, dict] = {}
    for path in document_paths:
        documents_content[path] = {}
        with open(path, "r") as f:
            documents_content[path]["content"] = f.read()
    return documents_content


def load_documents(folder_path: Path, pdf: bool = False) -> dict[Path, dict]:
    logger.info(f"Loading documents from '{folder_path}'")

    document_paths = get_document_paths(folder_path)
    if pdf:
        documents = get_pdf_documents_content(document_paths)
    else:
        documents = get_txt_documents_content(document_paths)

    logger.info(f"Found {len(documents)} documents")
    return documents
