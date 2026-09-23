from typing import Protocol

from app.domain.projects import Project


class ProjectRepositoryPort(Protocol):
    async def create_project(
        self, 
        name: str, 
        description: str, 
        client_id: str, 
        start_date: str, 
        end_date: str,
        cover_image_id: str | None = None
    ) -> Project:
        ...

    async def get_project(
        self,
        project_id: str
    ) -> Project | None:
        ...

    async def list_projects(
        self
    ) -> list[Project]:
        ...