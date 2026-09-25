from pydantic import BaseModel


class SupplierSummary(BaseModel):
    id: str
    name: str
    email: str
    phone: str | None = None


class ListSuppliersOutput(BaseModel):
    count: int
    data: list[SupplierSummary]