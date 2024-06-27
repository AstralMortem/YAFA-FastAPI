from ..schemas.gym import MuscleFrontCreate
from ..models.exercises import EquipmentExerciseRel, Exercise, MuscleExerciseRel
from ..utils.repository import Model, PrimaryKey, SQLAlchemyRepository
from ..database import sessionmanager


class ExerciseRepository(SQLAlchemyRepository[Exercise]):
    def __init__(self, *args, **kwargs):
        super().__init__(Exercise, *args, **kwargs)

    async def insert_exercise_relations(
        self,
        exercise_id: PrimaryKey,
        relations: list[dict],
        table: type[MuscleExerciseRel] | type[EquipmentExerciseRel],
    ):
        async with sessionmanager.session() as session:
            for rel in relations:
                session.add(table(exercise_id=exercise_id, **rel))
            await session.commit()
