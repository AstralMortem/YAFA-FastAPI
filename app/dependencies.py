from typing import Annotated
from fastapi import Depends
from .utils.repositories import (
    EquipmentRepository,
    ExercisesRepository,
    MuscleRepository,
)
from .services.gym import ExerciseService, EquipmentService, MuscleService
from .services.auth import fastapi_users
from .models.auth import User

secured_route: Annotated[User, Depends()] = Depends(
    fastapi_users.current_user(active=True)
)

exercise_service: Annotated[ExerciseService, Depends()] = Depends(
    lambda: ExerciseService(ExercisesRepository)
)

equipment_service: Annotated[EquipmentService, Depends()] = Depends(
    lambda: EquipmentService(EquipmentRepository)
)

muscle_service: Annotated[MuscleService, Depends()] = Depends(
    lambda: MuscleService(MuscleRepository)
)
