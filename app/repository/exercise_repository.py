from sqlalchemy import select
from typing import Any, Tuple

from sqlalchemy import BinaryExpression
from sqlalchemy.orm import selectinload
from sqlalchemy.sql.base import ExecutableOption

from ..models.gym import Equipment
from ..models.exercises import EquipmentExerciseRel, Exercise, MuscleExerciseRel
from .mixin import PrimaryKey, SQLAlchemyRepository
from ..database import sessionmanager


class ExerciseRepository(SQLAlchemyRepository[Exercise]):
    model = Exercise

    async def create(self, data: dict[str, Any]):
        async with sessionmanager.session() as session:
            equipment_list = data.pop("equipments")
            muscle_list = data.pop("muscles")
            instance = self.model(**data)
            for item in equipment_list:
                instance.equipments_association.append(EquipmentExerciseRel(**item))

            for item in muscle_list:
                instance.muscles_association.append(MuscleExerciseRel(**item))

            session.add(instance)
            await session.commit()
            await session.refresh(instance)
            return instance
