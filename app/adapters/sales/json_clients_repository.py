import json
from pathlib import Path

import aiofiles

from app.domain.sales import Client, ClientRepositoryPort


class JSONClientRepositoryAdapter(ClientRepositoryPort):
    def __init__(self, path: Path):
        self.path = path
        self.data = {}

        with open(self.path, "r") as f:
            self.data = json.load(f)


    async def get_client(self, client_id: str) -> Client | None:
        client_data = self.data.get(client_id)
        if client_data is None:
            return None
        return Client(**client_data)


    async def search_client_by_email(self, email: str) -> Client | None:
        for client_data in self.data.values():
            if client_data.get("email") == email:
                return Client(**client_data)
        return None


    async def create_client(
        self, 
        name: str, 
        email: str,
        phone: str | None = None,
        address: str | None = None
    ) -> Client:
        client_id = str(len(self.data) + 1)
        client_data = {
            "client_id": client_id,
            "name": name,
            "email": email,
            "phone": phone,
            "address": address
        }
        self.data[client_id] = client_data
        async with aiofiles.open(self.path, "w") as f:
            await f.write(json.dumps(self.data, indent=4))
        return Client(**client_data)


    async def list_clients(self) -> list[Client]:
        clients = []
        for client_data in self.data.values():
            clients.append(Client(**client_data))
        return clients