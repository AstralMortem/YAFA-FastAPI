from typing import Annotated
from fastapi import APIRouter, Depends
from ..dependencies import muscle_service
from ..schemas.gym import MuscleCreate, MuscleRead, MuscleUpdate


router = APIRouter(prefix="/muscles", tags=["muscles"])


@router.get("")
async def gets_muscles(service: muscle_service):
    return await service.filter()


@router.get("/{muscle_id}")
async def get_muscle(muscle_id: int, service: muscle_service):
    return await service.get(muscle_id)


@router.post("")
async def add_muscle(data: Annotated[MuscleCreate, Depends()], service: muscle_service):
    return await service.add(data)


@router.patch("/{muscle_id}")
async def update_muscle(
    id: int, data: Annotated[MuscleUpdate, Depends()], service: muscle_service
):
    return await service.update(id, data)


@router.delete("/{muscle_id}")
async def delete_muscle(id: int, service: muscle_service):
    return await service.delete(id)
