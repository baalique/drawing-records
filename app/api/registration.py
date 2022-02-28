from typing import Iterable, List, Optional

from fastapi import APIRouter, Depends, HTTPException, status

from app.db import app_db
from app.domain.services import registration as registration_services
from app.infrastructure.adapters.repositories.protocols import Repository
from app.service_layer.dtos.registration import RegistrationCreate, RegistrationDtoOut

router = APIRouter(prefix="/registration", tags=["registration"])

registration_repo = lambda: app_db.repositories["Registration"]


@router.post(
    "/new",
    response_model=RegistrationDtoOut,
    status_code=status.HTTP_201_CREATED,
    responses={201: {"description": "Item created"}},
)
async def create_registration(
    registration: RegistrationCreate,
    db: Repository = Depends(registration_repo),
) -> RegistrationDtoOut:
    return await registration_services.create_registration(db.add, dto=registration)


@router.get(
    "/all",
    response_model=List[RegistrationDtoOut],
    status_code=status.HTTP_200_OK,
    responses={200: {"description": "Items found"}},
)
async def get_all_registrations(
    db: Repository = Depends(registration_repo),
) -> Iterable[RegistrationDtoOut]:
    return await registration_services.get_all_registrations(db.list)


@router.get(
    "/{id}",
    response_model=RegistrationDtoOut,
    status_code=status.HTTP_200_OK,
    responses={
        200: {"description": "Item found"},
        404: {"description": "Item not found"},
    },
)
async def get_registration(
    id: int, db: Repository = Depends(registration_repo)
) -> Optional[RegistrationDtoOut]:
    registration = await registration_services.get_registration_by_id(db.get, id=id)
    if registration is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Item not found"
        )
    return registration
