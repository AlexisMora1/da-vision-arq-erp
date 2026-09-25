from app.domain.suppliers import (
    CreateSupplierItemRequest,
    SupplierItemsRepositoryPort,
    SuppliersRepositoryPort,
    create_supplier_item,
)
from app.workflows.exceptions_handler import exceptions_handler
from app.workflows.suppliers.create_supplier_item.models import (
    CreateSupplierItemInput,
    CreateSupplierItemOutput,
    SupplierItemCreated,
)


@exceptions_handler
async def create_supplier_item_workflow(
    supplier_id: str,
    request: CreateSupplierItemInput,
    suppliers_repository: SuppliersRepositoryPort,
    items_repository: SupplierItemsRepositoryPort,
) -> CreateSupplierItemOutput:
    result = await create_supplier_item(
        request=CreateSupplierItemRequest(
            supplier_id=supplier_id,
            sku=request.sku,
            name=request.name,
            description=request.description,
            unit=request.unit,
            unit_price=request.unit_price,
            currency=request.currency,
            active=request.active,
        ),
        suppliers_repository=suppliers_repository,
        items_repository=items_repository,
    )
    item = result.item
    return CreateSupplierItemOutput(
        message="Supplier item created successfully",
        data=SupplierItemCreated(**item.__dict__),
    )
