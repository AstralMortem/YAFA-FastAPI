from .repository.exercise_repository import ExerciseRepository
from .services.exercise_service import ExerciseService
from .repository.muscle_repository import MuscleRepository
from .services.muscle_service import MuscleService
from .repository.equipment_repository import EquipmentRepository
from .services.equipment_service import EquipmentService
from .services.auth import fastapi_users
from typing import Annotated
from fastapi import Depends
from .models.auth import User


secured_route: Annotated[User, Depends()] = Depends(
    fastapi_users.current_user(active=True)
)


def get_equipment_service():
    return EquipmentService(EquipmentRepository)


equipment_service = Annotated[EquipmentService, Depends(get_equipment_service)]


def get_muscle_service():
    return MuscleService(MuscleRepository)


muscle_service = Annotated[MuscleService, Depends(get_muscle_service)]


def get_exercise_service():
    return ExerciseService(ExerciseRepository)


exercise_service = Annotated[ExerciseService, Depends(get_exercise_service)]
