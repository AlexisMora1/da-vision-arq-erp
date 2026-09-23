from pydantic import BaseModel

from app.domain.sales.models import Client


class ListClientsOutput(BaseModel):
    count: int
    data: list[Client]