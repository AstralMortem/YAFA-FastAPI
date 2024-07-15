from uuid import UUID
from sqlalchemy import insert

from ..utils.sql import replace_column_in_dict

from ..utils.enums import MuscleEnum

from ..schemas.muscle_schema import MuscleReadDTO, MuscleReadRelDTO
from ..models.exercises import EquipmentExerciseRel, Exercise, MuscleExerciseRel
from .mixin import BaseService
from ..repository.exercise_repository import ExerciseRepository
from ..schemas.exercise_schema import (
    ExerciseCreateDTO,
    ExerciseReadDTO,
    ExerciseListDTO,
    ExerciseUpdateDTO,
)


class ExerciseService(
    BaseService[
        Exercise,
        ExerciseCreateDTO,
        ExerciseUpdateDTO,
        ExerciseListDTO,
        ExerciseReadDTO,
    ]
):
    def __init__(self, repository: type[ExerciseRepository]):
        self.repository = repository()
        self.list_dto = ExerciseListDTO
        self.read_dto = ExerciseReadDTO

    async def get_item(self, pk: str | int | UUID):
        instance = await self.repository.get(pk)
        muscles: list[MuscleReadRelDTO] = []
        for muscle in instance.muscles_association:
            muscles.append(
                MuscleReadRelDTO(
                    procent=muscle.procent,
                    type=MuscleEnum(muscle.type),
                    id=muscle.muscle.id,
                    image=muscle.muscle.image,
                    title=muscle.muscle.title,
                )
            )
        data = {**instance.__dict__}
        data["muscles"] = muscles
        data["equipments"] = instance.equipments
        return ExerciseReadDTO.model_validate(data)

    async def update_item(self, pk: str | int | UUID, data: ExerciseUpdateDTO):
        instance = await self.repository.update(pk, data.model_dump())
        muscles: list[MuscleReadRelDTO] = []
        for muscle in instance.muscles_association:
            muscles.append(
                MuscleReadRelDTO(
                    procent=muscle.procent,
                    type=MuscleEnum(muscle.type),
                    id=muscle.muscle.id,
                    image=muscle.muscle.image,
                    title=muscle.muscle.title,
                )
            )
        new_data = {**instance.__dict__}
        new_data["muscles"] = muscles
        new_data["equipments"] = instance.equipments
        return ExerciseReadDTO.model_validate(new_data)
