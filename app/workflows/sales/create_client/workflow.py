
from app.domain.sales import (
    ClientRepositoryPort,
    CreateClientRequest,
    create_client,
)
from app.workflows.exceptions_handler import exceptions_handler
from app.workflows.sales.create_client.models import (
    CreateClientInput,
    CreateClientOutput,
)


@exceptions_handler
async def create_client_workflow(
    request: CreateClientInput,
    clients_repository: ClientRepositoryPort
) -> CreateClientOutput:
    client = await create_client(
        request=CreateClientRequest(
            name=request.name,
            email=request.email,
            phone=request.phone,
            address=request.address
        ),
        client_repository=clients_repository
    )

    return CreateClientOutput(
        client_id=client.client_id,
        name=client.name,
        email=client.email,
        phone=client.phone,
        address=client.address
    )