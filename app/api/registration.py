from typing import List, Iterable, Optional

from fastapi import APIRouter, Depends, status, HTTPException

from adapters.repository import AbstractRepository
from app.domain.services import registration as registration_services
from db import app_db
from domain.entities.registration import Registration, RegistrationCreate

router = APIRouter(prefix="/registration", tags=["registration"])

registration_repo = app_db.repositories["Registration"]


@router.post(
    "/new",
    response_model=Registration,
    status_code=status.HTTP_201_CREATED,
    responses={201: {"description": "Item created"}}
)
async def create_registration(registration: RegistrationCreate,
                              db: AbstractRepository = Depends(registration_repo)) -> Registration:
    return await registration_services.create_registration(db.add, dto=registration)


@router.get(
    "/all",
    response_model=List[Registration],
    status_code=status.HTTP_200_OK,
    responses={200: {"description": "Items found"}}
)
async def get_all_registrations(db: AbstractRepository = Depends(registration_repo)) -> Iterable[Registration]:
    return await registration_services.get_all_registrations(db.list)


@router.get(
    "/{id}",
    response_model=Registration,
    status_code=status.HTTP_200_OK,
    responses={
        200: {"description": "Item found"},
        404: {"description": "Item not found"}
    }
)
async def get_registration(id: int, db: AbstractRepository = Depends(registration_repo)) -> Optional[Registration]:
    registration = await registration_services.get_registration_by_id(db.get, id=id)
    if registration is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    return registration
