from typing import Annotated
from fastapi import APIRouter, Depends

from ..schemas.routine_schema import RoutineCreateDTO, RoutineUpdateDTO


from ..dependencies import routine_service

router = APIRouter(prefix="/routines", tags=["Routines"])


@router.get("")
async def gets_routines(service: routine_service):
    return await service.get_items()


@router.get("/{routine_id}")
async def get_routine(routine_id: int, service: routine_service):
    return await service.get_item(routine_id)


@router.post("")
async def add_routine(
    data: Annotated[RoutineCreateDTO, Depends()], service: routine_service
):
    return await service.create_item(data)


@router.patch("/{routine_id}")
async def update_routine(
    id: int, data: Annotated[RoutineUpdateDTO, Depends()], service: routine_service
):
    return await service.update_item(id, data)


@router.delete("/{routine_id}")
async def delete_routine(id: int, service: routine_service):
    return await service.delete_item(id)
