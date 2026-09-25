from app.domain.suppliers.errors import (
    InvalidSupplierItemError,
    SupplierAlreadyExistsError,
    SupplierItemAlreadyExistsError,
    SupplierItemNotFoundError,
    SupplierNotFoundError,
)
from app.domain.suppliers.models import (
    CreateSupplierItemRequest,
    CreateSupplierItemResponse,
    CreateSupplierRequest,
    CreateSupplierResponse,
    GetSupplierItemRequest,
    GetSupplierItemResponse,
    GetSupplierRequest,
    GetSupplierResponse,
    ListSupplierItemsResponse,
    ListSuppliersResponse,
)
from app.domain.suppliers.ports import (
    SupplierItemsRepositoryPort,
    SuppliersRepositoryPort,
)

ALLOWED_UNITS = {"piece", "kilogram", "liter", "meter", "hour", "service", "package"}
ALLOWED_CURRENCIES = {"MXN", "USD", "EUR"}


async def get_supplier(
    request: GetSupplierRequest,
    suppliers_repository: SuppliersRepositoryPort,
) -> GetSupplierResponse:
    """Retrieve a supplier by its ID.

    Args:
        request (GetSupplierRequest): The request object containing the supplier ID.
        suppliers_repository (SuppliersRepositoryPort): The repository to interact with supplier data.

    Returns:
        GetSupplierResponse: The response object containing the retrieved supplier.
    """

    supplier = await suppliers_repository.get_supplier_by_id(request.supplier_id)

    if not supplier:
        raise SupplierNotFoundError(f"Supplier with ID {request.supplier_id} not found")

    return GetSupplierResponse(
        id=supplier.id,
        name=supplier.name,
        email=supplier.email,
        phone=supplier.phone,
    )


async def list_suppliers(
    suppliers_repository: SuppliersRepositoryPort,
) -> ListSuppliersResponse:
    """Retrieve a list of all suppliers.

    Args:
        suppliers_repository (SuppliersRepositoryPort): The repository to interact with supplier data.

    Returns:
        ListSuppliersResponse: The response object containing the list of suppliers.
    """
    suppliers = await suppliers_repository.list_suppliers()
    return ListSuppliersResponse(
        suppliers=suppliers,
    )


async def create_supplier(
    request: CreateSupplierRequest,
    suppliers_repository: SuppliersRepositoryPort,
) -> CreateSupplierResponse:
    """Create a new supplier.

    Args:
        request (CreateSupplierRequest): The request object containing the supplier details.
        suppliers_repository (SuppliersRepositoryPort): The repository to interact with supplier data.

    Returns:
        CreateSupplierResponse: The response object containing the created supplier.
    """
    suspect = await suppliers_repository.get_supplier_by_email(request.email)

    if suspect:
        raise SupplierAlreadyExistsError(
            f"Supplier with email {request.email} already exists"
        )

    supplier = await suppliers_repository.create_supplier(
        name=request.name,
        email=request.email,
        phone=request.phone,
    )

    return CreateSupplierResponse(
        id=supplier.id,
        name=supplier.name,
        email=supplier.email,
        phone=supplier.phone,
    )


async def create_supplier_item(
    request: CreateSupplierItemRequest,
    suppliers_repository: SuppliersRepositoryPort,
    items_repository: SupplierItemsRepositoryPort,
) -> CreateSupplierItemResponse:
    supplier = await suppliers_repository.get_supplier_by_id(request.supplier_id)
    if supplier is None:
        raise SupplierNotFoundError(f"Supplier with ID {request.supplier_id} not found")

    if request.unit not in ALLOWED_UNITS:
        raise InvalidSupplierItemError(f"Unit '{request.unit}' is not supported")
    if request.currency not in ALLOWED_CURRENCIES:
        raise InvalidSupplierItemError(
            f"Currency '{request.currency}' is not supported"
        )
    if request.unit_price < 0:
        raise InvalidSupplierItemError("Unit price cannot be negative")
    if request.sku and await items_repository.get_supplier_item_by_sku(
        request.supplier_id, request.sku
    ):
        raise SupplierItemAlreadyExistsError(
            f"Supplier item with SKU {request.sku} already exists"
        )

    item = await items_repository.create_supplier_item(
        supplier_id=request.supplier_id,
        sku=request.sku,
        name=request.name,
        description=request.description,
        unit=request.unit,
        unit_price=request.unit_price,
        currency=request.currency,
        active=request.active,
    )
    return CreateSupplierItemResponse(item=item)


async def get_supplier_item(
    request: GetSupplierItemRequest,
    suppliers_repository: SuppliersRepositoryPort,
    items_repository: SupplierItemsRepositoryPort,
) -> GetSupplierItemResponse:
    supplier = await suppliers_repository.get_supplier_by_id(request.supplier_id)
    if supplier is None:
        raise SupplierNotFoundError(f"Supplier with ID {request.supplier_id} not found")

    item = await items_repository.get_supplier_item(
        request.supplier_id, request.item_id
    )
    if item is None:
        raise SupplierItemNotFoundError(
            f"Supplier item with ID {request.item_id} not found"
        )
    return GetSupplierItemResponse(item=item)


async def list_supplier_items(
    supplier_id: str,
    suppliers_repository: SuppliersRepositoryPort,
    items_repository: SupplierItemsRepositoryPort,
) -> ListSupplierItemsResponse:
    supplier = await suppliers_repository.get_supplier_by_id(supplier_id)
    if supplier is None:
        raise SupplierNotFoundError(f"Supplier with ID {supplier_id} not found")
    return ListSupplierItemsResponse(
        items=await items_repository.list_supplier_items(supplier_id)
    )
