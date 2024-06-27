from typing import Annotated
from uuid import UUID
from fastapi import APIRouter, Depends

from app.schemas.exercises import ExerciseCreate, ExerciseUpdate
from ..dependencies import exercise_service

router = APIRouter(prefix="/exercises", tags=["Exercises"])


@router.get("")
async def get_all_exercises(service: exercise_service):
    return await service.get_joined_exercises()


@router.get("/{exercise_id}")
async def get_exercise(exercise_id: UUID, service: exercise_service):
    return await service.get_joined_exercise_by_id(exercise_id)


@router.post("")
async def insert_exercise(
    data: Annotated[ExerciseCreate, Depends()], service: exercise_service
):
    return await service.add(data)


@router.patch("/{exercise_id}")
async def update_exercise(
    exercise_id: UUID,
    data: Annotated[ExerciseUpdate, Depends()],
    service: exercise_service,
):
    return await service.update(exercise_id, data)


@router.delete("/{exercise_id}")
async def delete_exercise(exercise_id: UUID, service: exercise_service):
    return await service.delete(exercise_id)
