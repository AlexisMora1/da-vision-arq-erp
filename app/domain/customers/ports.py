from typing import Protocol

from app.domain.customers.models import Client


class ClientRepositoryPort(Protocol):
    async def create_client(
        self, 
        name: str, 
        email: str,
        phone: str | None = None,
        address: str | None = None
    ) -> Client:
        ...

    async def get_client(self, client_id: str) -> Client | None:
        ...

    async def search_client_by_email(self, email: str) -> Client | None:
        ...

    async def list_clients(self) -> list[Client]:
        ...