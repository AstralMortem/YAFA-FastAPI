from sqlalchemy.ext.asyncio import AsyncSession
from ..utils.repository import SQLAlchemyRepository
from ..models.gym import Equipment, Muscle


class EquipmentRepository(SQLAlchemyRepository[Equipment]):
    def __init__(self, model: type[Equipment], session: AsyncSession, *args, **kwargs):
        super(EquipmentRepository, self).__init__(model, session, *args, **kwargs)


class MuscleRepository(SQLAlchemyRepository[Muscle]):
    def __init__(self, model: type[Muscle], session: AsyncSession, *args, **kwargs):
        super(MuscleRepository, self).__init__(model, session, *args, **kwargs)
