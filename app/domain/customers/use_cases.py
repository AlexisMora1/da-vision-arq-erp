from app.domain.customers.errors import ClientAlreadyExistsError, ClientNotFoundError
from app.domain.customers.models import Client, CreateClientRequest, GetClientRequest
from app.domain.customers.ports import ClientRepositoryPort


async def create_client(
    request: CreateClientRequest,
    client_repository: ClientRepositoryPort
) -> Client:
    """Create a new client.

    Args:
        request (CreateClientRequest): The client data to create.
        client_repository (ClientRepositoryPort): The repository to store the client in.

    Returns:
        Client: The created client.
    """
    registered = await client_repository.search_client_by_email(email=request.email)

    if registered:
        raise ClientAlreadyExistsError(f"Client with email '{request.email}' already exists.")

    client = await client_repository.create_client(
        name=request.name,
        email=request.email,
        phone=request.phone,
        address=request.address,
    )
    
    return client


async def get_client(
    request: GetClientRequest,
    client_repository: ClientRepositoryPort
) -> Client:
    """Retrieve a client by their ID.

    Args:
        request (GetClientRequest): The request containing the client ID.
        client_repository (ClientRepositoryPort): The repository to fetch the client from.

    Returns:
        Client: The client if found.
    """
    client = await client_repository.get_client(client_id=request.client_id)

    if not client: 
        raise ClientNotFoundError(f"Client with ID '{request.client_id}' not found.")
    
    return client
