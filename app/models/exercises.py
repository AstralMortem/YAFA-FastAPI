from uuid import UUID
from sqlalchemy import Enum, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .mixins import BaseTable, CommonUUIDMixin, TimestampMixin
from ..utils.enums import ExerciseTypeEnum, MuscleEnum
from .gym import Muscle, Equipment


class Exercise(CommonUUIDMixin, BaseTable):
    __tablename__ = "exercises"
    title: Mapped[str]
    level: Mapped[int] = mapped_column(default=1)
    type: Mapped[Enum] = mapped_column(Enum(ExerciseTypeEnum))
    description: Mapped[str | None] = mapped_column(default=None)
    instruction: Mapped[str | None] = mapped_column(default=None)
    image: Mapped[str | None] = mapped_column(default=None)
    author_id: Mapped[UUID | None] = mapped_column(ForeignKey("user.id"), default=None)
    is_public: Mapped[bool] = mapped_column(default=False)

    # relations
    equipments: Mapped[list["Equipment"]] = relationship(
        secondary="equipment_exercise_rel", lazy="selectin"
    )
    muscles: Mapped[list["Muscle"]] = relationship(
        secondary="muscle_exercise_rel", lazy="selectin"
    )


class EquipmentExerciseRel(TimestampMixin, BaseTable):
    __tablename__ = "equipment_exercise_rel"
    equipment_id: Mapped[int] = mapped_column(
        ForeignKey("equipments.id"), primary_key=True
    )
    exercise_id: Mapped[UUID] = mapped_column(
        ForeignKey("exercises.id"), primary_key=True
    )


class MuscleExerciseRel(TimestampMixin, BaseTable):
    __tablename__ = "muscle_exercise_rel"
    muscle_id: Mapped[int] = mapped_column(ForeignKey("muscles.id"), primary_key=True)
    exercise_id: Mapped[UUID] = mapped_column(
        ForeignKey("exercises.id"), primary_key=True
    )
    procent: Mapped[int] = mapped_column(default=1)  # from 1 to 100
    type: Mapped[Enum] = mapped_column(Enum(MuscleEnum))
