from app.domain.suppliers import SuppliersRepositoryPort
from app.workflows.exceptions_handler import exceptions_handler
from app.workflows.suppliers.list_suppliers.models import (
    ListSuppliersOutput,
    SupplierSummary,
)


@exceptions_handler
async def list_suppliers_workflow(
    suppliers_repository: SuppliersRepositoryPort
) -> ListSuppliersOutput:
    suppliers = []
    pre = await suppliers_repository.list_suppliers()

    for supplier in pre:
        suppliers.append(
            SupplierSummary(
                id=supplier.id,
                name=supplier.name,
                email=supplier.email,
                phone=supplier.phone
            )
        )
        
    return ListSuppliersOutput(
        count=len(suppliers), 
        data=suppliers
    )