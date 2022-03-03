from typing import Iterable, List, Optional

from fastapi import APIRouter, Depends, Response, status

from app.infrastructure.adapters.repositories.drawing import SQLAlchemyDrawingRepository
from app.infrastructure.adapters.repositories.protocols.entities import (
    DrawingRepository,
)
from app.service_layer.dtos.drawing import (
    DrawingDtoCreate,
    DrawingDtoOut,
    DrawingDtoUpdate,
)
from app.service_layer.services import drawing as drawing_services

router = APIRouter(prefix="/drawing", tags=["drawing"])

drawing_repo = SQLAlchemyDrawingRepository


@router.post(
    "/new",
    response_model=DrawingDtoOut,
    status_code=status.HTTP_201_CREATED,
    responses={
        201: {"description": "Item created"},
        422: {"description": "Item already exists"},
    },
)
async def create_drawing(
    drawing: DrawingDtoCreate, repo: DrawingRepository = Depends(drawing_repo)
) -> DrawingDtoOut:
    return await drawing_services.create_drawing(drawing, repo)


@router.get(
    "/all",
    response_model=List[DrawingDtoOut],
    status_code=status.HTTP_200_OK,
    responses={200: {"description": "Items found"}},
)
async def get_all_drawings(
    repo: DrawingRepository = Depends(drawing_repo),
) -> Iterable[DrawingDtoOut]:
    return await drawing_services.get_all_drawings(repo)


@router.get(
    "/{id}",
    response_model=DrawingDtoOut,
    status_code=status.HTTP_200_OK,
    responses={
        200: {"description": "Item found"},
        404: {"description": "Item not found"},
    },
)
async def get_drawing(
    id: int, repo: DrawingRepository = Depends(drawing_repo)
) -> Optional[DrawingDtoOut]:
    drawing = await drawing_services.get_drawing_by_id(id, repo)
    return drawing


@router.patch(
    "/{id}",
    response_model=DrawingDtoOut,
    status_code=status.HTTP_200_OK,
    responses={
        200: {"description": "Item updated"},
        404: {"description": "Item not found"},
    },
)
async def update_drawing(
    id: int,
    drawing: DrawingDtoUpdate,
    repo: DrawingRepository = Depends(drawing_repo),
) -> Optional[DrawingDtoOut]:
    updated_drawing = await drawing_services.update_drawing(id, drawing, repo)
    return updated_drawing


@router.delete(
    "/{id}",
    status_code=status.HTTP_204_NO_CONTENT,
    responses={404: {"description": "Item not found"}},
)
async def delete_drawing(
    id: int, repo: DrawingRepository = Depends(drawing_repo)
) -> Response:
    await drawing_services.delete_drawing(id, repo)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
