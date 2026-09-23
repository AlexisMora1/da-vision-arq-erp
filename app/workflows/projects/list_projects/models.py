from datetime import date

from pydantic import BaseModel


class ProjectSummary(BaseModel):
    project_id: str
    name: str
    description: str
    client_id: str
    cover_image_url: str | None
    start_date: date
    end_date: date


class ListProjectsOutput(BaseModel):
    count: int
    data: list[ProjectSummary]