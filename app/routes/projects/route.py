from typing import Annotated

from fastapi import APIRouter, Depends

from app.dependencies import (
    get_client_repository,
    get_file_repository,
    get_project_repository,
)
from app.domain.customers import ClientRepositoryPort
from app.domain.projects import ProjectRepositoryPort
from app.domain.storage import FileRepositoryPort
from app.workflows.projects import (
    CreateProjectInput,
    CreateProjectOutput,
    GetProjectInput,
    GetProjectOuput,
    ListProjectsOutput,
    create_project_workflow,
    get_project_workflow,
    list_projects_workflow,
)

router = APIRouter(
    tags=["Projects"],
)

@router.get("/projects/{project_id}")
async def get_project(
    project_id: str,
    project_repository: Annotated[ProjectRepositoryPort, Depends(get_project_repository)],
    client_repository: Annotated[ClientRepositoryPort, Depends(get_client_repository)],
    file_repository: Annotated[FileRepositoryPort, Depends(get_file_repository)],
) -> GetProjectOuput:
    return await get_project_workflow(
        request=GetProjectInput(project_id=project_id),
        project_repository=project_repository,
        clients_repository=client_repository,
        file_repository=file_repository
    )


@router.post("/projects")
async def create_project(
    request: CreateProjectInput,
    project_repository: Annotated[ProjectRepositoryPort, Depends(get_project_repository)],
    client_repository: Annotated[ClientRepositoryPort, Depends(get_client_repository)],
) -> CreateProjectOutput:
    return await create_project_workflow(
        request=request,
        project_repository=project_repository,
        client_repository=client_repository
    )


@router.get("/projects")
async def list_projects(
    project_repository: Annotated[ProjectRepositoryPort, Depends(get_project_repository)],
    file_repository: Annotated[FileRepositoryPort, Depends(get_file_repository)],
) -> ListProjectsOutput:
    return await list_projects_workflow(
        project_repository=project_repository,
        file_repository=file_repository
    )

