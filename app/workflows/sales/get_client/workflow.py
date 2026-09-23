from app.domain.sales import ClientRepositoryPort, GetClientRequest, get_client
from app.workflows.exceptions_handler import exceptions_handler
from app.workflows.sales.get_client.models import GetClientInput, GetClientOutput


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