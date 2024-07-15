from .mixin import SQLAlchemyRepository
from ..models.routines import Routine


class RoutineRepository(SQLAlchemyRepository[Routine]):
    model = Routine
