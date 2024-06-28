from pydantic import BaseModel, ConfigDict
from .mixin import CommonDTOMixin


class MuscleCreateDTO(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    title: str
    image: str | None = None


class MuscleUpdateDTO(MuscleCreateDTO): ...


class MuscleListDTO(MuscleCreateDTO):
    id: int


class MuscleReadDTO(CommonDTOMixin, MuscleListDTO): ...
