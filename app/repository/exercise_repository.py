from ..models.exercises import Exercise
from .mixin import SQLAlchemyRepository


class ExerciseRepository(SQLAlchemyRepository[Exercise]):
    model = Exercise

    # async def filter(
    #     self,
    #     conditions: Tuple[BinaryExpression] | None,
    #     options: Tuple[ExecutableOption] | None,
    # ):
    #     q = select(self.model)
    #     return await super().filter(q, None)

    # async def create(self, data: ExerciseCreateDTO):

    #     equipments = data.equipments
    #     instance = await super().create(**data.model_dump(exclude={"equipments"}))

    #     q = insert(EquipmentExerciseRel).values([{"equipment_id": id, "exercise_id": instance.id} for id  in equipments])
    #     async with sessionmanager.session() as session:
    #         await session.execute(q)
