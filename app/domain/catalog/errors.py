from app.domain.errors import DomainError


class ProductNotFoundError(DomainError):
    http_status = 404