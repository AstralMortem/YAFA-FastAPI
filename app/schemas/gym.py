from datetime import datetime
from pydantic import BaseModel, ConfigDict


class BaseGym(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    title: str
    image: str | None = None


class EquipmentCreate(BaseGym): ...


class EquipmentUpdate(EquipmentCreate): ...


class EquipmentRead(EquipmentCreate):
    id: int
    created_at: datetime
    updated_at: datetime | None


class MuscleCreate(BaseGym): ...


class MuscleUpdate(MuscleCreate): ...


class MuscleRead(MuscleCreate):
    id: int
    created_at: datetime
    updated_at: datetime | None
