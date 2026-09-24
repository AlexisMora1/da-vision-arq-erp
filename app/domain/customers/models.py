from dataclasses import dataclass


@dataclass
class Client:
    client_id: str
    name: str
    email: str
    phone: str | None = None
    address: str | None = None


@dataclass
class GetClientRequest:
    client_id: str


@dataclass
class CreateClientRequest:
    name: str
    email: str | None = None
    phone: str | None = None
    address: str | None = None

