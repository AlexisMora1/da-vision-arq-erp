from pydantic import BaseModel


class SupplierItemSummary(BaseModel):
    id: str
    supplier_id: str
    sku: str | None
    name: str
    description: str
    unit: str
    unit_price: float
    currency: str
    active: bool


class ListSupplierItemsOutput(BaseModel):
    count: int
    data: list[SupplierItemSummary]
