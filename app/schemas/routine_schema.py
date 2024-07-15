from uuid import UUID
from pydantic import BaseModel, ConfigDict
from .mixin import CommonDTOMixin


class RoutineCreateDTO(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    title: str
    is_public: bool = True
    author_id: UUID | None = None


class RoutineReadDTO(CommonDTOMixin, RoutineCreateDTO):
    id: UUID


class RoutineListDTO(RoutineCreateDTO):
    id: UUID


class RoutineUpdateDTO(RoutineCreateDTO): ...
