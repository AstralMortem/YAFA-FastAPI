from ..models.gym import Muscle
from ..schemas.muscle_schema import (
    MuscleCreateDTO,
    MuscleListDTO,
    MuscleReadDTO,
    MuscleUpdateDTO,
)
from ..repository.muscle_repository import MuscleRepository
from .mixin import BaseService


class MuscleService(
    BaseService[
        Muscle,
        MuscleCreateDTO,
        MuscleUpdateDTO,
        MuscleListDTO,
        MuscleReadDTO,
    ]
):
    def __init__(self, repository: type[MuscleRepository]):
        self.repository = repository()
