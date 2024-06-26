from typing import Annotated
from fastapi import Depends
from .services.auth import fastapi_users
from .models.auth import User
from .services.gym import EquipmentService, MuscleService
from .services.exercises import ExerciseService
from .repositories.gym import EquipmentRepository, MuscleRepository
from .repositories.exercises import ExerciseRepository


secured_route: Annotated[User, Depends()] = Depends(
    fastapi_users.current_user(active=True)
)

equipment_service = Annotated[
    EquipmentService,
    Depends(lambda: EquipmentService(EquipmentRepository)),
]

muscle_service = Annotated[
    MuscleService,
    Depends(lambda: MuscleService(MuscleRepository)),
]

exercise_service = Annotated[
    ExerciseService,
    Depends(lambda: ExerciseService(ExerciseRepository)),
]
