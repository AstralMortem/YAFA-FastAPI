from uuid import UUID
from pydantic import BaseModel, ConfigDict

from .muscle_schema import MuscleListDTO, MuscleReadDTO, MuscleReadRelDTO

from .equipment_schema import (
    EquipmentExerciseCreateDTO,
    EquipmentListDTO,
    MuscleExerciseCreateDTO,
)
from .mixin import ActiveDTOMixin, CommonDTOMixin
from ..utils.enums import ExerciseTypeEnum


class ExerciseCreateDTO(ActiveDTOMixin, BaseModel):
    model_config = ConfigDict(from_attributes=True)
    title: str
    level: int = 1
    type: ExerciseTypeEnum
    description: str | None = None
    instruction: str | None = None
    image: str | None = None
    author_id: UUID | None = None
    is_public: bool = False
    equipments: list[EquipmentExerciseCreateDTO] = []
    muscles: list[MuscleExerciseCreateDTO] = []


class ExerciseListDTO(ExerciseCreateDTO):
    id: UUID
    equipments: list[EquipmentListDTO] = []
    muscles: list[MuscleListDTO] = []


class ExerciseUpdateDTO(ExerciseCreateDTO): ...


class ExerciseReadDTO(CommonDTOMixin, ExerciseListDTO):
    muscles: list[MuscleReadRelDTO] = []
