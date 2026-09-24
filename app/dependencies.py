from pathlib import Path

from app.adapters.catalog import JSONProductsRepositoryAdapter
from app.adapters.customers import JSONClientRepositoryAdapter
from app.adapters.projects import JSONProjectRepositoryAdapter
from app.adapters.storage import LocalFileRepositoryAdapter


def get_project_repository() -> JSONProjectRepositoryAdapter:
    return JSONProjectRepositoryAdapter(path=Path("data/projects.json"))

def get_client_repository() -> JSONClientRepositoryAdapter:
    return JSONClientRepositoryAdapter(path=Path("data/clients.json"))

def get_file_repository() -> LocalFileRepositoryAdapter:
    return LocalFileRepositoryAdapter(storage_dir=Path("data/files"), base_url="http://localhost:8000")

def get_products_repository() -> JSONProductsRepositoryAdapter:
    return JSONProductsRepositoryAdapter(path=Path("data/products.json"))