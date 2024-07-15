from typing import Annotated
from fastapi import APIRouter, Depends

from ..schemas.muscle_schema import MuscleCreateDTO, MuscleUpdateDTO
from ..dependencies import muscle_service


router = APIRouter(prefix="/muscles", tags=["muscles"])


@router.get("")
async def gets_muscles(service: muscle_service):
    return await service.get_items()


@router.get("/{muscle_id}")
async def get_muscle(muscle_id: int, service: muscle_service):
    return await service.get_item(muscle_id)


@router.post("")
async def add_muscle(
    data: Annotated[MuscleCreateDTO, Depends()], service: muscle_service
):
    return await service.create_item(data)


@router.patch("/{muscle_id}")
async def update_muscle(
    id: int, data: Annotated[MuscleUpdateDTO, Depends()], service: muscle_service
):
    return await service.update_item(id, data)


@router.delete("/{muscle_id}")
async def delete_muscle(id: int, service: muscle_service):
    return await service.delete_item(id)
