from typing import Iterable, List, Optional

from fastapi import APIRouter, Depends, Response, status

from app.api.exceptions import map_exception
from app.infrastructure.protocols import UnitOfWork
from app.service_layer.dtos.drawing import (
    DrawingDtoCreate,
    DrawingDtoOut,
    DrawingDtoUpdate,
)
from app.service_layer.exceptions import AlreadyExistsError, NotFoundError
from app.service_layer.services import drawing as drawing_services

router = APIRouter(prefix="/drawing", tags=["drawing"])


@router.post(
    "/new",
    response_model=DrawingDtoOut,
    status_code=status.HTTP_201_CREATED,
    responses={
        201: {"description": "Item created"},
        404: {"description": "Item not found"},
        409: {"description": "Item already exists"},
    },
)
async def create_drawing(
    drawing: DrawingDtoCreate,
    uow: UnitOfWork = Depends(),
) -> DrawingDtoOut:
    try:
        return await drawing_services.create_drawing(drawing, uow)
    except (AlreadyExistsError, NotFoundError) as ex:
        raise map_exception(ex)


@router.get(
    "/all",
    response_model=List[DrawingDtoOut],
    status_code=status.HTTP_200_OK,
    responses={200: {"description": "Items found"}},
)
async def get_all_drawings(
    uow: UnitOfWork = Depends(),
) -> Iterable[DrawingDtoOut]:
    return await drawing_services.get_all_drawings(uow)


@router.get(
    "/{id}",
    response_model=DrawingDtoOut,
    status_code=status.HTTP_200_OK,
    responses={
        200: {"description": "Item found"},
        404: {"description": "Item not found"},
    },
)
async def get_drawing(id: int, uow: UnitOfWork = Depends()) -> DrawingDtoOut:
    try:
        return await drawing_services.get_drawing_by_id(id, uow)
    except NotFoundError as ex:
        raise map_exception(ex)


@router.patch(
    "/{id}",
    response_model=DrawingDtoOut,
    status_code=status.HTTP_200_OK,
    responses={
        200: {"description": "Item updated"},
        404: {"description": "Item not found"},
        409: {"description": "Item already exists"},
    },
)
async def update_drawing(
    id: int,
    drawing: DrawingDtoUpdate,
    uow: UnitOfWork = Depends(),
) -> Optional[DrawingDtoOut]:
    try:
        return await drawing_services.update_drawing(id, drawing, uow)
    except (AlreadyExistsError, NotFoundError) as ex:
        raise map_exception(ex)


@router.delete(
    "/{id}",
    status_code=status.HTTP_204_NO_CONTENT,
    responses={
        204: {"description": "Item deleted"},
        404: {"description": "Item not found"},
    },
)
async def delete_drawing(id: int, uow: UnitOfWork = Depends()) -> Response:
    try:
        await drawing_services.delete_drawing(id, uow)
    except (AlreadyExistsError, NotFoundError) as ex:
        raise map_exception(ex)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
