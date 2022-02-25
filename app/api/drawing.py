from typing import Iterable, List, Optional

from fastapi import APIRouter, Depends, HTTPException, Response, status

from app.db import app_db
from app.domain.entities.drawing import Drawing, DrawingCreate, DrawingUpdate
from app.domain.services import drawing as drawing_services
from app.infrastructure.adapters.repositories.fake.drawing import FakeDrawingRepository

router = APIRouter(prefix="/drawing", tags=["drawing"])

drawing_repo = lambda: app_db.repositories["Drawing"]


@router.post(
    "/new",
    response_model=Drawing,
    status_code=status.HTTP_201_CREATED,
    responses={201: {"description": "Item created"}},
)
async def create_drawing(
    drawing: DrawingCreate, db: FakeDrawingRepository = Depends(drawing_repo)
) -> Drawing:
    return await drawing_services.create_drawing(db.add, dto=drawing)


@router.get(
    "/all",
    response_model=List[Drawing],
    status_code=status.HTTP_200_OK,
    responses={200: {"description": "Items found"}},
)
async def get_all_drawings(
    db: FakeDrawingRepository = Depends(drawing_repo),
) -> Iterable[Drawing]:
    return await drawing_services.get_all_drawings(db.list)


@router.get(
    "/{id}",
    response_model=Drawing,
    status_code=status.HTTP_200_OK,
    responses={
        200: {"description": "Item found"},
        404: {"description": "Item not found"},
    },
)
async def get_drawing(
    id: int, db: FakeDrawingRepository = Depends(drawing_repo)
) -> Optional[Drawing]:
    drawing = await drawing_services.get_drawing_by_id(db.get, id=id)
    if drawing is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Item not found"
        )
    return drawing


@router.patch(
    "/{id}",
    response_model=Drawing,
    status_code=status.HTTP_200_OK,
    responses={
        200: {"description": "Item updated"},
        404: {"description": "Item not found"},
    },
)
async def update_drawing(
    id: int, drawing: DrawingUpdate, db: FakeDrawingRepository = Depends(drawing_repo)
) -> Drawing:
    updated_drawing = await drawing_services.update_drawing(
        db.update, dto=drawing, id=id
    )
    if updated_drawing is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Item not found"
        )
    return updated_drawing


@router.delete(
    "/{id}",
    status_code=status.HTTP_204_NO_CONTENT,
    responses={404: {"description": "Item not found"}},
)
async def delete_drawing(
    id: int, db: FakeDrawingRepository = Depends(drawing_repo)
) -> Response:
    res = await drawing_services.delete_drawing(db.delete, id=id)
    if not res:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Item not found"
        )
    return Response(status_code=status.HTTP_204_NO_CONTENT)
