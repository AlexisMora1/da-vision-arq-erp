from app.domain.projects import ProjectRepositoryPort
from app.domain.storage import (
    FileRepositoryPort,
    GetDownloadFileUrlRequest,
    get_download_file_url,
)
from app.workflows.exceptions_handler import exceptions_handler
from app.workflows.projects.list_projects.models import (
    ListProjectsOutput,
    ProjectSummary,
)


@exceptions_handler
async def list_projects_workflow(
    project_repository: ProjectRepositoryPort,
    file_repository: FileRepositoryPort,
) -> ListProjectsOutput:
    projects = await project_repository.list_projects()

    summaries = []
    for project in projects:
        cover_image_url = None
        if project.cover_image_id is not None:
            cover_image = await get_download_file_url(
                request=GetDownloadFileUrlRequest(file_id=project.cover_image_id),
                file_repository=file_repository
            )
            cover_image_url = cover_image.url

        summaries.append(
            ProjectSummary(
                project_id=project.project_id,
                name=project.name,
                description=project.description,
                client_id=project.client_id,
                cover_image_url=cover_image_url,
                start_date=project.start_date,
                end_date=project.end_date
            )
        )

    return ListProjectsOutput(
        count=len(summaries),
        data=summaries
    )