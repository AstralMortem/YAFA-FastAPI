from uuid import UUID
from pydantic import BaseModel, ConfigDict
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


class ExerciseListDTO(ExerciseCreateDTO):
    id: UUID


class ExerciseUpdateDTO(ExerciseCreateDTO): ...


class ExerciseReadDTO(CommonDTOMixin, ExerciseListDTO): ...
