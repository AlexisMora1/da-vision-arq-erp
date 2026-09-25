from app.domain.suppliers.ports import SuppliersRepositoryPort
from app.domain.suppliers.use_cases import CreateSupplierRequest, create_supplier
from app.workflows.exceptions_handler import exceptions_handler
from app.workflows.suppliers.create_supplier.models import (
    CreatedSupplier,
    CreateSupplierInput,
    CreateSupplierOutput,
)


@exceptions_handler
async def create_supplier_workflow(
    input: CreateSupplierInput,
    suppliers_repository: SuppliersRepositoryPort,
) -> CreateSupplierOutput:
    supplier = await create_supplier(
        request=CreateSupplierRequest(
            name=input.name,
            email=input.email,
            phone=input.phone,
        ),
        suppliers_repository=suppliers_repository,
    )
    
    return CreateSupplierOutput(
        message="Supplier created successfully",
        data=CreatedSupplier(
            id=supplier.id,
            name=supplier.name,
            email=supplier.email,
            phone=supplier.phone,
        ),
    )