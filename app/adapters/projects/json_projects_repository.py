import json
from dataclasses import asdict
from datetime import date
from pathlib import Path
from uuid import uuid4

import aiofiles

from app.domain.projects import Project, ProjectRepositoryPort


class JSONProjectRepositoryAdapter(ProjectRepositoryPort):

    def __init__(self, path: Path):
        self.path = path
        self.data = {}
        try:
            with open(self.path, "r") as f:
                content = f.read()
        except FileNotFoundError:
            return

        if content.strip():
            self.data = json.loads(content)

    async def create_project(
        self, 
        name: str, 
        description: str, 
        client_id: str, 
        start_date: str, 
        end_date: str,
        cover_image_id: str | None = None
    ) -> Project:
        
        start_date = date.fromisoformat(start_date)
        end_date = date.fromisoformat(end_date)

        project = Project(
            project_id=str(uuid4()),
            name=name,
            description=description,
            client_id=client_id,
            start_date=start_date,
            end_date=end_date,
            cover_image_id=cover_image_id
        )

        self.data[project.project_id] = {
            **asdict(project),
            "start_date": project.start_date.isoformat(),
            "end_date": project.end_date.isoformat(),
        }

        async with aiofiles.open(self.path, "w") as f:
            await f.write(json.dumps(self.data, indent=4))

        return project

    async def get_project(
        self,
        project_id: str
    ) -> Project:
        project_data = self.data.get(project_id)
        if not project_data:
            return None

        return Project(
            project_id=project_data["project_id"],
            name=project_data["name"],
            description=project_data["description"],
            client_id=project_data["client_id"],
            start_date=date.fromisoformat(project_data["start_date"]),
            end_date=date.fromisoformat(project_data["end_date"]),
            cover_image_id=project_data.get("cover_image_id")
        )

    async def list_projects(
        self
    ) -> list[Project]:
        projects = []
        for project_data in self.data.values():
            projects.append(
                Project(
                    project_id=project_data["project_id"],
                    name=project_data["name"],
                    description=project_data["description"],
                    client_id=project_data["client_id"],
                    start_date=date.fromisoformat(project_data["start_date"]),
                    end_date=date.fromisoformat(project_data["end_date"]),
                    cover_image_id=project_data.get("cover_image_id")
                )
            )
        return projects