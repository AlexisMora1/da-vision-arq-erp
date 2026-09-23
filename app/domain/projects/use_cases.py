from app.domain.projects.models import (
    CreateProjectRequest,
    CreateProjectResponse,
    Project,
)
from app.domain.projects.ports import ProjectRepositoryPort


async def create_project(
    request: CreateProjectRequest, 
    projects_repository: ProjectRepositoryPort
) -> CreateProjectResponse:
    """Create a new project using the provided request and project repository.

    Args:
        request (CreateProjectRequest): The request object containing project details.
        projects_repository (ProjectRepositoryPort): The repository to interact with project data.

    Returns:
        CreateProjectResponse: The response object containing the created project's details, including the cover image ID if provided.
    """

    project: Project = await projects_repository.create_project(
        name=request.name,
        description=request.description,
        client_id=request.client_id,
        start_date=request.start_date,
        end_date=request.end_date,
        cover_image_id=request.cover_image_id
        
    )
    
    return CreateProjectResponse(
        project_id=project.project_id,
        name=project.name,
        description=project.description,
        client_id=project.client_id,
        start_date=project.start_date,
        end_date=project.end_date,
        cover_image_id=project.cover_image_id
    )