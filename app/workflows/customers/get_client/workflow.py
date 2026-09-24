from app.domain.customers import ClientRepositoryPort, GetClientRequest, get_client
from app.workflows.customers.get_client.models import GetClientInput, GetClientOutput
from app.workflows.exceptions_handler import exceptions_handler


@exceptions_handler
async def get_client_workflow(
    request: GetClientInput,
    client_repository: ClientRepositoryPort,
) -> GetClientOutput:
    client = await get_client(
        request=GetClientRequest(client_id=request.client_id),
        client_repository=client_repository
    )

    return GetClientOutput(
        data=client
    )