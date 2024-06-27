from sqlalchemy import func, select
from sqlalchemy.orm import joinedload, load_only, selectinload
from ..utils.enums import MuscleEnum

from ..schemas.gym import EquipmentFrontCreate, MuscleFrontCreate, MuscleFrontRead

from ..utils.repository import PrimaryKey

from ..models.gym import Equipment, Muscle
from ..models.exercises import EquipmentExerciseRel, Exercise, MuscleExerciseRel
from ..utils.service import BaseCRUDService
from ..schemas.exercises import (
    ExerciseCreate,
    ExerciseRead,
    ExerciseList,
    ExerciseUpdate,
)


class ExerciseService(
    BaseCRUDService[ExerciseCreate, ExerciseUpdate, ExerciseRead, ExerciseList]
):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.read_model = ExerciseRead
        self.list_model = ExerciseList

    async def get_joined_exercises(self):
        statement = select(Exercise).options(
            load_only(
                Exercise.id,
                Exercise.title,
                Exercise.level,
                Exercise.image,
                Exercise.is_active,
                Exercise.is_public,
            )
            .selectinload(Exercise.muscle_details)
            .load_only(MuscleExerciseRel.muscle_id)
            .joinedload(MuscleExerciseRel.muscle)
            .load_only(Muscle.title)
        )
        rows = await self.repository.custom(statement)
        result = []
        rows = rows.scalars()
        for row in rows:
            muscles_list = [M.muscle.title for M in row.muscle_details]
            row.__dict__["muscles"] = muscles_list
            result.append(ExerciseList.model_validate(row))
        return result

    async def get_joined_exercise_by_id(self, pk: PrimaryKey):
        statement = (
            select(Exercise)
            .where(Exercise.id == pk)
            .limit(1)
            .options(
                selectinload(Exercise.equipments).load_only(
                    Equipment.id, Equipment.title, Equipment.image
                ),
                selectinload(Exercise.muscle_details).joinedload(
                    MuscleExerciseRel.muscle
                ),
            )
        )
        result = await self.repository.custom(statement)
        result = result.scalar_one_or_none()
        if not result:
            raise Exception("No model")

        muscles_details = []
        for res in result.muscle_details:
            muscles_details.append(
                MuscleFrontRead(
                    procent=res.procent,
                    type=MuscleEnum(res.type),
                    id=res.muscle_id,
                    title=res.muscle.title,
                    image=res.muscle.image,
                )
            )
        result.__dict__["muscle_details"] = muscles_details

        return ExerciseRead.model_validate(result)

    async def create_exercise(self, data: ExerciseCreate):
        data_dict = data.model_dump().pop("muscles").pop("equipments")
        muscles: list[MuscleFrontCreate] = data.muscles
        equipments: list[EquipmentFrontCreate] = data.equipments
        instance = await self.repository.create(data_dict)
        await self.insert_exercise_relations(
            instance.id, [m.model_dump() for m in muscles], MuscleExerciseRel
        )
        await self.insert_exercise_relations(
            instance.id, [m.model_dump() for m in equipments], EquipmentExerciseRel
        )
