from ..schemas.muscle_schema import (
    MuscleCreateDTO,
    MuscleListDTO,
    MuscleReadDTO,
    MuscleUpdateDTO,
)
from .mixin import SQLAlchemyRepository
from ..models.gym import Muscle


class MuscleRepository(
    SQLAlchemyRepository[
        Muscle,
        MuscleCreateDTO,
        MuscleUpdateDTO,
        MuscleListDTO,
        MuscleReadDTO,
    ]
):
    model = Muscle
    dto_read_model = MuscleReadDTO
    dto_list_model = MuscleListDTO
