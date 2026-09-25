import json
from dataclasses import asdict
from pathlib import Path
from uuid import uuid4

import aiofiles

from app.domain.suppliers import SupplierItem, SupplierItemsRepositoryPort


class JSONSupplierItemsRepositoryAdapter(SupplierItemsRepositoryPort):
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

    async def get_supplier_item(
        self, supplier_id: str, item_id: str
    ) -> SupplierItem | None:
        item_data = self.data.get(item_id)
        if item_data is None or item_data.get("supplier_id") != supplier_id:
            return None
        return SupplierItem(**item_data)

    async def get_supplier_item_by_sku(
        self, supplier_id: str, sku: str
    ) -> SupplierItem | None:
        for item_data in self.data.values():
            if (
                item_data.get("supplier_id") == supplier_id
                and item_data.get("sku") == sku
            ):
                return SupplierItem(**item_data)
        return None

    async def list_supplier_items(self, supplier_id: str) -> list[SupplierItem]:
        return [
            SupplierItem(**item_data)
            for item_data in self.data.values()
            if item_data.get("supplier_id") == supplier_id
        ]

    async def create_supplier_item(
        self,
        supplier_id: str,
        sku: str | None,
        name: str,
        description: str,
        unit: str,
        unit_price: float,
        currency: str,
        active: bool = True,
    ) -> SupplierItem:
        item = SupplierItem(
            id=str(uuid4()),
            supplier_id=supplier_id,
            sku=sku,
            name=name,
            description=description,
            unit=unit,
            unit_price=unit_price,
            currency=currency,
            active=active,
        )
        self.data[item.id] = asdict(item)

        async with aiofiles.open(self.path, "w") as file:
            await file.write(json.dumps(self.data, indent=4))

        return item
