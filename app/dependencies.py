from typing import Annotated
from fastapi import Depends

from .utils.repositories import ExercisesRepository

from .services.exercises import ExercisesService
from .services.auth import fastapi_users
from .models.auth import User

secured_route: Annotated[User, Depends()] = Depends(
    fastapi_users.current_user(active=True)
)

exercise_service: Annotated[ExercisesService, Depends()] = Depends(
    lambda: ExercisesService(ExercisesRepository)
)
