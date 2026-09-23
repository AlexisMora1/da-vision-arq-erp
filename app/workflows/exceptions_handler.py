import functools
import logging
from collections.abc import Awaitable, Callable
from typing import ParamSpec, TypeVar

from fastapi import HTTPException

from app.domain.errors import DomainError

logger = logging.getLogger(__name__)

P = ParamSpec("P")
T = TypeVar("T")


def exceptions_handler(workflow: Callable[P, Awaitable[T]]) -> Callable[P, Awaitable[T]]:
    """Translate domain errors raised by a workflow into HTTPException responses."""

    @functools.wraps(workflow)
    async def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
        try:
            return await workflow(*args, **kwargs)
        except DomainError as error:
            raise HTTPException(status_code=error.http_code, detail=str(error)) from error
        except Exception as error:
            # Log the real cause server-side; never leak internals to the client.
            logger.exception("Unhandled error in workflow '%s'", workflow.__name__)
            raise HTTPException(status_code=500, detail="Internal server error") from error

    return wrapper
