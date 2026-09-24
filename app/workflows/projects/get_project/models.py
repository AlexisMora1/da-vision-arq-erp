from datetime import date

from pydantic import BaseModel

from app.domain.customers import Client


class ProjectDetails(BaseModel):
    project_id: str
    name: str
    description: str
    client: Client
    cover_image_url: str | None
    start_date: date
    end_date: date


class GetProjectInput(BaseModel):
    project_id: str


class GetProjectOuput(BaseModel):
    data: ProjectDetails