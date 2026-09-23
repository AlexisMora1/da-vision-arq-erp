
from app.domain.catalog import (
    verify_product_in_catalog,
    verify_service_in_catalog,
)
from app.domain.identity import (
    verify_user_in_identity,
)
from app.workflows.exceptions_handler import exceptions_handler
from app.workflows.sales.create_sales_order.models import (
    CreateSalesOrderInput,
    CreateSalesOrderOutput,
)


@exceptions_handler
async def create_sales_order_workflow(request: CreateSalesOrderInput) -> CreateSalesOrderOutput:

    verify_user_in_identity(request.user_id, request.tenant_id)

    for product in request.products:
        verify_product_in_catalog(product.id, request.tenant_id)

    for service in request.services:
        verify_service_in_catalog(service.id, request.tenant_id)


    # Implement the workflow logic here
    return CreateSalesOrderOutput(status="success")