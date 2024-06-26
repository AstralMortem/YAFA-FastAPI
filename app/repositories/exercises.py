from ..models.exercises import Exercise
from ..utils.repository import SQLAlchemyRepository


class ExerciseRepository(SQLAlchemyRepository[Exercise]):
    def __init__(self, *args, **kwargs):
        super().__init__(Exercise, *args, **kwargs)
