from app.domain.suppliers import GetSupplierRequest, get_supplier
from app.domain.suppliers.ports import SuppliersRepositoryPort
from app.workflows.exceptions_handler import exceptions_handler
from app.workflows.suppliers.get_supplier.models import (
    GetSupplierInput,
    GetSupplierOutput,
    SupplierDetails,
)


@exceptions_handler
async def get_supplier_workflow(input_data: GetSupplierInput, suppliers_repository: SuppliersRepositoryPort) -> GetSupplierOutput:
    
    supplier = await get_supplier(
        request=GetSupplierRequest(supplier_id=input_data.supplier_id),
        suppliers_repository=suppliers_repository
    )
    return GetSupplierOutput(
        data=SupplierDetails(
            id=supplier.id,
            name=supplier.name,
            email=supplier.email,
            phone=supplier.phone,
        )
    )