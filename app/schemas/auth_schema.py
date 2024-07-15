from datetime import datetime
from uuid import UUID
from fastapi_users import schemas
from ..utils.enums import GenderEnum, TrainingAimEnum


class UserRead(schemas.BaseUser[UUID]):
    full_name: str
    age: int
    gender: GenderEnum
    height: int
    weight: int
    training_time: int
    training_per_week: int
    training_aim: TrainingAimEnum
    rest_time: int
    created_at: datetime
    updated_at: datetime | None


class UserCreate(schemas.BaseUserCreate):
    full_name: str
    age: int
    gender: GenderEnum
    height: int
    weight: int
    training_time: int
    training_per_week: int
    training_aim: TrainingAimEnum
    rest_time: int


class UserUpdate(schemas.BaseUserUpdate):
    full_name: str
    age: int
    height: int
    weight: int
    training_time: int
    training_per_week: int
    training_aim: TrainingAimEnum
    rest_time: int
