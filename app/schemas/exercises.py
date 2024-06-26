from datetime import datetime
from uuid import UUID
from pydantic import BaseModel, ConfigDict

from ..utils.enums import ExerciseTypeEnum

from .gym import MuscleRead, EquipmentRead, MuscleCreate, EquipmentCreate


class ExerciseCreate(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    title: str
    level: int = 1
    type: ExerciseTypeEnum
    description: str | None = None
    instruction: str | None = None
    image: str | None = None
    author_id: UUID | None = None
    is_public: bool = False
    is_active: bool = True
    equipments: list[EquipmentCreate] = []
    muscles: list[MuscleCreate] = []


class ExerciseUpdate(ExerciseCreate):
    pass


class ExerciseRead(ExerciseCreate):
    id: UUID
    created_at: datetime
    updated_at: datetime | None
    equipments: list[EquipmentRead] = []
    muscles: list[MuscleRead] = []


class ExerciseList(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: UUID
    title: str
    level: int
    image: str | None = None
    author_id: UUID | None = None
    is_public: bool = False
    is_active: bool = True
    equipments: list[EquipmentRead] = []
    muscles: list[MuscleRead] = []
