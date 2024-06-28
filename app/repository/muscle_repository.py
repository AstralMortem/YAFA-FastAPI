from .mixin import SQLAlchemyRepository
from ..models.gym import Muscle


class MuscleRepository(SQLAlchemyRepository[Muscle]):
    model = Muscle
