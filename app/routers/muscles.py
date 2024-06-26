from typing import Annotated
from fastapi import APIRouter, Depends
from ..dependencies import muscle_service
from ..schemas.gym import MuscleCreate, MuscleRead, MuscleUpdate


router = APIRouter(prefix="/muscles", tags=["muscles"])


@router.get("")
async def gets_muscles(service=muscle_service) -> list[MuscleRead]:
    return await service.gets_muscles()


@router.get("/{muscle_id}")
async def get_muscle(muscle_id: int, service=muscle_service) -> MuscleRead | None:
    return await service.get_muscle(muscle_id)


@router.post("")
async def add_muscle(
    data: Annotated[MuscleCreate, Depends()], service=muscle_service
) -> MuscleRead:
    return await service.add_muscle(data)


@router.patch("/{muscle_id}")
async def update_muscle(
    id: int, data: Annotated[MuscleUpdate, Depends()], service=muscle_service
) -> MuscleRead:
    return await service.update_muscle(id, data)


@router.delete("/{muscle_id}")
async def delete_muscle(id: int, service=muscle_service) -> MuscleRead:
    return await service.delete_muscle(id)
