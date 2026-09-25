from pydantic import BaseModel


class GetSupplierItemInput(BaseModel):
    supplier_id: str
    item_id: str


class SupplierItemDetails(BaseModel):
    id: str
    supplier_id: str
    sku: str | None
    name: str
    description: str
    unit: str
    unit_price: float
    currency: str
    active: bool


class GetSupplierItemOutput(BaseModel):
    data: SupplierItemDetails
