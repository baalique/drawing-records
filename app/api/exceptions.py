from typing import Dict

from fastapi import HTTPException, status

from app.service_layer.exceptions import ServiceLayerException

_exceptions_mapping: Dict[str, int] = {
    "NotFoundError": status.HTTP_404_NOT_FOUND,
    "AlreadyExistsError": status.HTTP_409_CONFLICT,
}


def map_exception(exception: ServiceLayerException) -> HTTPException:
    return HTTPException(
        status_code=_exceptions_mapping[exception.__class__.__name__],
        detail=str(exception),
    )
