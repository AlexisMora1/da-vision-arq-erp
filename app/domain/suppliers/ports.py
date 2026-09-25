from typing import Protocol

from app.domain.suppliers.models import Supplier, SupplierItem


class SuppliersRepositoryPort(Protocol):
    async def get_supplier_by_id(self, supplier_id: str) -> Supplier | None:
        ...

    async def get_supplier_by_email(self, email: str) -> Supplier | None:
        ...

    async def list_suppliers(self) -> list[Supplier]:
        ...

    async def create_supplier(self, name: str, email: str, phone: str | None = None) -> Supplier:
        ...


class SupplierItemsRepositoryPort(Protocol):
    async def get_supplier_item(self, supplier_id: str, item_id: str) -> SupplierItem | None:
        ...

    async def get_supplier_item_by_sku(self, supplier_id: str, sku: str) -> SupplierItem | None:
        ...

    async def list_supplier_items(self, supplier_id: str) -> list[SupplierItem]:
        ...

    async def create_supplier_item(
        self,
        supplier_id: str,
        sku: str | None,
        name: str,
        description: str,
        unit: str,
        unit_price: float,
        currency: str,
        active: bool = True,
    ) -> SupplierItem:
        ...