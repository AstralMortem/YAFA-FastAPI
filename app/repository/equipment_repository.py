from ..models.gym import Equipment
from .mixin import SQLAlchemyRepository


class EquipmentRepository(SQLAlchemyRepository[Equipment]):
    model = Equipment
