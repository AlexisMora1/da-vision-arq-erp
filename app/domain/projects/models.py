from dataclasses import dataclass
from datetime import date

from app.domain.projects.errors import InvalidProjectDatesError


@dataclass
class Project:
    project_id: str
    name: str
    description: str
    client_id: str
    start_date: date
    end_date: date
    cover_image_id: str | None = None

    def __post_init__(self) -> None:
        if self.end_date < self.start_date:
            raise InvalidProjectDatesError()


@dataclass
class CreateProjectRequest:
    name: str
    description: str
    client_id: str
    start_date: str
    end_date: str
    cover_image_id: str | None = None


@dataclass
class CreateProjectResponse:
    project_id: str
    name: str
    description: str
    client_id: str
    start_date: str
    end_date: str
    cover_image_id: str | None = None