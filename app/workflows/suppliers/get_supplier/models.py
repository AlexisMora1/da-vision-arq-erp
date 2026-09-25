from pydantic import BaseModel


class SupplierDetails(BaseModel):
    id: str
    name: str
    email: str
    phone: str | None = None


class GetSupplierInput(BaseModel):
    supplier_id: str


class GetSupplierOutput(BaseModel):
    data: SupplierDetails