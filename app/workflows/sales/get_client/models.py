from pydantic import BaseModel

from app.domain.sales import Client


class GetClientInput(BaseModel):
    client_id: str

class GetClientOutput(BaseModel):
    data: Client