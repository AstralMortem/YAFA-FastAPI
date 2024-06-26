from ..utils.repository import SQLAlchemyRepository
from ..models.gym import Equipment, Muscle


class EquipmentRepository(SQLAlchemyRepository[Equipment]):
    def __init__(self, *args, **kwargs):
        super(EquipmentRepository, self).__init__(Equipment, *args, **kwargs)


class MuscleRepository(SQLAlchemyRepository[Muscle]):
    def __init__(self, *args, **kwargs):
        super(MuscleRepository, self).__init__(Muscle, *args, **kwargs)
