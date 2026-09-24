from pydantic import BaseModel

from app.domain.customers.models import Client


class ListClientsOutput(BaseModel):
    count: int
    data: list[Client]