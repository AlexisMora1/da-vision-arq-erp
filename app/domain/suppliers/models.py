from dataclasses import dataclass


@dataclass
class Supplier:
    id: str
    name: str
    email: str
    phone: str | None = None


@dataclass
class CreateSupplierRequest:
    name: str
    email: str
    phone: str | None = None


@dataclass
class CreateSupplierResponse:
    id: str
    name: str
    email: str
    phone: str | None = None


@dataclass
class GetSupplierRequest:
    supplier_id: str


@dataclass
class GetSupplierResponse:
    id: str
    name: str
    email: str
    phone: str | None = None


@dataclass
class ListSuppliersResponse:
    suppliers: list[Supplier]


@dataclass
class SupplierItem:
    id: str
    supplier_id: str
    sku: str | None
    name: str
    description: str
    unit: str
    unit_price: float
    currency: str
    active: bool = True


@dataclass
class CreateSupplierItemRequest:
    supplier_id: str
    sku: str | None
    name: str
    description: str
    unit: str
    unit_price: float
    currency: str
    active: bool = True


@dataclass
class CreateSupplierItemResponse:
    item: SupplierItem


@dataclass
class GetSupplierItemRequest:
    supplier_id: str
    item_id: str


@dataclass
class GetSupplierItemResponse:
    item: SupplierItem


@dataclass
class ListSupplierItemsResponse:
    items: list[SupplierItem]