from ..models.gym import Equipment
from .mixin import BaseService
from ..schemas.equipment_schema import (
    EquipmentCreateDTO,
    EquipmentUpdateDTO,
    EquipmentListDTO,
    EquipmentReadDTO,
)
from ..repository.equipment_repository import EquipmentRepository


class EquipmentService(
    BaseService[
        Equipment,
        EquipmentCreateDTO,
        EquipmentUpdateDTO,
        EquipmentListDTO,
        EquipmentReadDTO,
    ]
):
    def __init__(self, repository: type[EquipmentRepository]):
        self.repository = repository()
        self.list_dto = EquipmentListDTO
        self.read_dto = EquipmentReadDTO
