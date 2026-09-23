class DomainError(Exception):
    """Base class for domain errors that carry an HTTP status code for translation."""

    http_code: int = 400

    def __init__(self, message: str | None = None) -> None:
        super().__init__(message or self.__class__.__name__)
