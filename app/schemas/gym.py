from datetime import datetime
from pydantic import BaseModel, ConfigDict
from ..utils.enums import MuscleEnum


class BaseGym(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    title: str
    image: str | None = None


class EquipmentCreate(BaseGym): ...


class EquipmentUpdate(EquipmentCreate): ...


class EquipmentRead(EquipmentCreate):
    id: int


class MuscleCreate(BaseGym): ...


class MuscleUpdate(MuscleCreate): ...


class MuscleRead(MuscleCreate):
    id: int


class MuscleFrontRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    procent: int
    type: MuscleEnum
    id: int
    title: str
    image: str | None = None
