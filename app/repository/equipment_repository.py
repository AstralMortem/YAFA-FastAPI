from ..schemas.equipment_schema import (
    EquipmentCreateDTO,
    EquipmentListDTO,
    EquipmentReadDTO,
    EquipmentUpdateDTO,
)
from ..models.gym import Equipment
from .mixin import SQLAlchemyRepository


class EquipmentRepository(
    SQLAlchemyRepository[
        Equipment,
        EquipmentCreateDTO,
        EquipmentUpdateDTO,
        EquipmentListDTO,
        EquipmentReadDTO,
    ]
):
    model = Equipment
    dto_read_model = EquipmentReadDTO
    dto_list_model = EquipmentListDTO
