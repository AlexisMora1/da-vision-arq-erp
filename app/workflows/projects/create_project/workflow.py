from app.domain.projects import (
    ProjectRepositoryPort,
    create_project,
)
from app.domain.sales import (
    ClientRepositoryPort,
    GetClientRequest,
    get_client,
)
from app.workflows.exceptions_handler import exceptions_handler
from app.workflows.projects.create_project.models import (
    CreateProjectInput,
    CreateProjectOutput,
)


@exceptions_handler
async def create_project_workflow(
    request: CreateProjectInput,
    project_repository: ProjectRepositoryPort,
    client_repository: ClientRepositoryPort
) -> CreateProjectOutput:

    _ = await get_client(
        request=GetClientRequest(client_id=request.client_id),
        client_repository=client_repository
    )
    
    project = await create_project(
        request=request,
        projects_repository=project_repository
    )

    return CreateProjectOutput(
        project_id=project.project_id,
        name=project.name,
        description=project.description,
        client_id=project.client_id,
        start_date=project.start_date,
        end_date=project.end_date,
        cover_image_id=project.cover_image_id
    )