from typing import Annotated
from uuid import UUID
from fastapi import APIRouter, Depends

from ..schemas.exercise_schema import ExerciseCreateDTO, ExerciseUpdateDTO
from ..dependencies import exercise_service

router = APIRouter(prefix="/exercises", tags=["Exercises"])


@router.get("")
async def get_all_exercises(service: exercise_service):
    return await service.get_items()


@router.get("/{exercise_id}")
async def get_exercise(exercise_id: UUID, service: exercise_service):
    return await service.get_item(exercise_id)


@router.post("")
async def insert_exercise(
    data: Annotated[ExerciseCreateDTO, Depends()], service: exercise_service
):
    return await service.create_item(data)


@router.patch("/{exercise_id}")
async def update_exercise(
    exercise_id: UUID,
    data: Annotated[ExerciseUpdateDTO, Depends()],
    service: exercise_service,
):
    return await service.update_item(exercise_id, data)


@router.delete("/{exercise_id}")
async def delete_exercise(exercise_id: UUID, service: exercise_service):
    return await service.delete_item(exercise_id)
