import json
from dataclasses import asdict
from pathlib import Path
from uuid import uuid4

import aiofiles

from app.domain.suppliers import Supplier, SuppliersRepositoryPort


class JSONSuppliersRepositoryAdapter(SuppliersRepositoryPort):
    def __init__(self, path: Path):
        self.path = path
        self.data = {}

        try:
            with open(self.path, "r") as file:
                content = file.read()
        except FileNotFoundError:
            content = "{}"

        if content.strip():
            self.data = json.loads(content)

    async def get_supplier_by_id(self, supplier_id: str) -> Supplier | None:
        supplier_data = self.data.get(supplier_id)
        if supplier_data is None:
            return None
        return Supplier(**supplier_data)

    async def get_supplier_by_email(self, email: str) -> Supplier | None:
        for supplier_data in self.data.values():
            if supplier_data.get("email") == email:
                return Supplier(**supplier_data)
        return None

    async def list_suppliers(self) -> list[Supplier]:
        return [Supplier(**supplier_data) for supplier_data in self.data.values()]

    async def create_supplier(
        self,
        name: str,
        email: str,
        phone: str | None = None,
    ) -> Supplier:
        supplier = Supplier(
            id=str(uuid4()),
            name=name,
            email=email,
            phone=phone,
        )
        self.data[supplier.id] = asdict(supplier)

        async with aiofiles.open(self.path, "w") as file:
            await file.write(json.dumps(self.data, indent=4))

        return supplier
