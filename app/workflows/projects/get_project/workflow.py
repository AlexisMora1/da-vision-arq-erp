from app.domain.projects import ProjectNotFoundError, ProjectRepositoryPort
from app.domain.sales import ClientRepositoryPort, GetClientRequest, get_client
from app.domain.storage import (
    FileRepositoryPort,
    GetDownloadFileUrlRequest,
    get_download_file_url,
)
from app.workflows.exceptions_handler import exceptions_handler
from app.workflows.projects.get_project.models import (
    GetProjectInput,
    GetProjectOuput,
    ProjectDetails,
)


@exceptions_handler
async def get_project_workflow(
    request: GetProjectInput, 
    project_repository: ProjectRepositoryPort,
    clients_repository: ClientRepositoryPort,
    file_repository: FileRepositoryPort,
) -> GetProjectOuput:
    project = await project_repository.get_project(request.project_id)
    
    if project is None:
        raise ProjectNotFoundError() 

    if project.cover_image_id is not None:
        cover_image = await get_download_file_url(
            request=GetDownloadFileUrlRequest(file_id=project.cover_image_id),
            file_repository=file_repository
        )

    client = await get_client(
        request=GetClientRequest(client_id=project.client_id),
        client_repository=clients_repository
    )

    return GetProjectOuput(
        data=ProjectDetails(
            project_id=project.project_id,
            name=project.name,
            description=project.description,
            client=client,
            start_date=project.start_date,
            end_date=project.end_date,
            cover_image_url=cover_image.url if project.cover_image_id is not None else None
        )
    )