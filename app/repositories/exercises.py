from sqlalchemy.ext.asyncio import AsyncSession
from ..schemas.gym import MuscleFrontCreate
from ..models.exercises import EquipmentExerciseRel, Exercise, MuscleExerciseRel
from ..utils.repository import Model, PrimaryKey, SQLAlchemyRepository
from ..database import sessionmanager


class ExerciseRepository(SQLAlchemyRepository[Exercise]):
    def __init__(self, model: type[Exercise], session: AsyncSession, *args, **kwargs):
        self.model = model
        self.session = session
        super().__init__(model, session, *args, **kwargs)

    async def insert_exercise_relations(
        self,
        exercise_id: PrimaryKey,
        relations: list[dict],
        table: type[MuscleExerciseRel] | type[EquipmentExerciseRel],
    ):
        for rel in relations:
            self.session.add(table(exercise_id=exercise_id, **rel))
        await self.session.commit()
