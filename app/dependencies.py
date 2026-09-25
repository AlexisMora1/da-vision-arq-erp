from pathlib import Path

from app.adapters.catalog import JSONProductsRepositoryAdapter
from app.adapters.customers import JSONClientRepositoryAdapter
from app.adapters.projects import JSONProjectRepositoryAdapter
from app.adapters.storage import LocalFileRepositoryAdapter
from app.adapters.suppliers import (
    JSONSupplierItemsRepositoryAdapter,
    JSONSuppliersRepositoryAdapter,
)


def get_project_repository() -> JSONProjectRepositoryAdapter:
    return JSONProjectRepositoryAdapter(path=Path("data/projects.json"))


def get_client_repository() -> JSONClientRepositoryAdapter:
    return JSONClientRepositoryAdapter(path=Path("data/clients.json"))


def get_file_repository() -> LocalFileRepositoryAdapter:
    return LocalFileRepositoryAdapter(
        storage_dir=Path("data/files"), base_url="http://localhost:8000"
    )


def get_products_repository() -> JSONProductsRepositoryAdapter:
    return JSONProductsRepositoryAdapter(path=Path("data/products.json"))


def get_suppliers_repository() -> JSONSuppliersRepositoryAdapter:
    return JSONSuppliersRepositoryAdapter(path=Path("data/suppliers.json"))


def get_supplier_items_repository() -> JSONSupplierItemsRepositoryAdapter:
    return JSONSupplierItemsRepositoryAdapter(path=Path("data/supplier_items.json"))
