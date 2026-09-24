

from app.domain.customers.ports import ClientRepositoryPort
from app.workflows.customers.list_clients.models import ListClientsOutput
from app.workflows.exceptions_handler import exceptions_handler


@exceptions_handler
async def list_clients_workflow(
    clients_repository: ClientRepositoryPort
) -> ListClientsOutput:
    clients = await clients_repository.list_clients()
    return ListClientsOutput(
        count=len(clients),
        data=clients
    )