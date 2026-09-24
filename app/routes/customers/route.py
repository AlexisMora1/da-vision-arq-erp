from typing import Annotated

from fastapi import APIRouter, Depends

from app.dependencies import get_client_repository
from app.domain.customers import ClientRepositoryPort
from app.workflows.customers import (
    CreateClientInput,
    CreateClientOutput,
    GetClientInput,
    GetClientOutput,
    ListClientsOutput,
    create_client_workflow,
    get_client_workflow,
    list_clients_workflow,
)

router = APIRouter(
    tags=["Sales"]
)


@router.get("/clients/{client_id}")
async def get_client(
    client_id: str,
    clients_repository: Annotated[ClientRepositoryPort, Depends(get_client_repository)]
) -> GetClientOutput:
    return await get_client_workflow(
        request=GetClientInput(client_id=client_id),
        client_repository=clients_repository
    )


@router.post("/clients")
async def create_client(
    request: CreateClientInput,
    clients_repository: Annotated[ClientRepositoryPort, Depends(get_client_repository)]
) -> CreateClientOutput:
    return await create_client_workflow(
        request=request,
        clients_repository=clients_repository
    )


@router.get("/clients")
async def list_clients(
    clients_repository: Annotated[ClientRepositoryPort, Depends(get_client_repository)]
) -> ListClientsOutput:
    return await list_clients_workflow(
        clients_repository=clients_repository
    )