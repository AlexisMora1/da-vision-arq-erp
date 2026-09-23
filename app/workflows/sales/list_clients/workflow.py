

from app.domain.sales.ports import ClientRepositoryPort
from app.workflows.exceptions_handler import exceptions_handler
from app.workflows.sales.list_clients.models import ListClientsOutput


@exceptions_handler
async def list_clients_workflow(
    clients_repository: ClientRepositoryPort
) -> ListClientsOutput:
    clients = await clients_repository.list_clients()
    return ListClientsOutput(
        count=len(clients),
        data=clients
    )