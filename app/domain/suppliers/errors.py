from app.domain.errors import DomainError


class SupplierNotFoundError(DomainError):
    http_code = 404


class SupplierAlreadyExistsError(DomainError):
    http_code = 409


class SupplierItemNotFoundError(DomainError):
    http_code = 404


class SupplierItemAlreadyExistsError(DomainError):
    http_code = 409


class InvalidSupplierItemError(DomainError):
    http_code = 422