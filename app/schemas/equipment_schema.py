from pydantic import BaseModel, ConfigDict
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
