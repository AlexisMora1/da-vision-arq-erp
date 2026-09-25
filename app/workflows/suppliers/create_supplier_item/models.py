from pydantic import BaseModel


class CreateSupplierItemInput(BaseModel):
    sku: str | None = None
    name: str
    description: str = ""
    unit: str
    unit_price: float
    currency: str
    active: bool = True


class SupplierItemCreated(BaseModel):
    id: str
    supplier_id: str
    sku: str | None
    name: str
    description: str
    unit: str
    unit_price: float
    currency: str
    active: bool


class CreateSupplierItemOutput(BaseModel):
    message: str
    data: SupplierItemCreated
