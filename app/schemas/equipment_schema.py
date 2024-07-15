from pydantic import BaseModel, ConfigDict

from ..utils.enums import MuscleEnum
from .mixin import CommonDTOMixin


class EquipmentCreateDTO(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    title: str
    image: str | None = None


class EquipmentUpdateDTO(EquipmentCreateDTO): ...


class EquipmentListDTO(EquipmentCreateDTO):
    id: int


class EquipmentReadDTO(CommonDTOMixin, EquipmentListDTO):
    id: int


class EquipmentExerciseCreateDTO(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    equipment_id: int


class MuscleExerciseCreateDTO(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    muscle_id: int
    procent: int = 1
    type: MuscleEnum
