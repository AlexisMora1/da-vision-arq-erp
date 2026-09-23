

from pydantic import BaseModel


class CreateSalesOrderInput(BaseModel):
    user_id: str
    tenant_id: str
    client_id: str
    products: list[str]
    services: list[str]


class CreateSalesOrderOutput(BaseModel):
    status: str