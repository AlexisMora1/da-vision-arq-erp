from pydantic import BaseModel


class CreatedSupplier(BaseModel):
    id: str
    name: str
    email: str
    phone: str | None = None


class CreateSupplierInput(BaseModel):
    name: str
    email: str
    phone: str | None = None


class CreateSupplierOutput(BaseModel):
    message: str
    data: CreatedSupplier