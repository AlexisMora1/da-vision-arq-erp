from pydantic import BaseModel


class CreateClientInput(BaseModel):
    name: str
    email: str
    phone: str | None = None
    address: str | None = None

class CreateClientOutput(BaseModel):
    client_id: str
    name: str
    email: str
    phone: str | None = None
    address: str | None = None