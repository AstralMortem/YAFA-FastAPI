from uuid import UUID
from pydantic import BaseModel, ConfigDict

from .equipment_schema import EquipmentReadDTO
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
    equipments: list[int] = []


class ExerciseListDTO(ExerciseCreateDTO):
    id: UUID
    equipments: list[EquipmentReadDTO] = []


class ExerciseUpdateDTO(ExerciseCreateDTO): ...


class ExerciseReadDTO(CommonDTOMixin, ExerciseListDTO): ...
