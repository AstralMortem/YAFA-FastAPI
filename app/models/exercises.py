from typing import TYPE_CHECKING
from uuid import UUID
from sqlalchemy import Enum, ForeignKey
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .mixins import BaseTable, CommonUUIDMixin, TimestampMixin
from ..utils.enums import ExerciseTypeEnum, MuscleEnum

if TYPE_CHECKING:
    from .gym import Muscle, Equipment
    from .routines import ExerciseRoutineRel


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

    # association between Exercise -> EquipmentExerciseRel
    equipments_association: Mapped[list["EquipmentExerciseRel"]] = relationship(
        back_populates="exercise",
        cascade="save-update, merge, delete, delete-orphan",
        lazy="selectin",
    )
    equipments = association_proxy("equipments_association", "equipment")

    # association between Exercise -> MuscleExerciseRel
    muscles_association: Mapped[list["MuscleExerciseRel"]] = relationship(
        back_populates="exercise",
        cascade="save-update, merge, delete, delete-orphan",
        lazy="selectin",
    )

    muscles = association_proxy("muscles_association", "muscle")

    # association between Exercise -> ExerciseRoutineRel -> Routine
    routine_association: Mapped[list["ExerciseRoutineRel"]] = relationship(
        back_populates="exercise",
        cascade="save-update, merge, delete, delete-orphan",
        lazy="selectin",
    )


class EquipmentExerciseRel(TimestampMixin, BaseTable):
    __tablename__ = "equipment_exercise_rel"
    equipment_id: Mapped[int] = mapped_column(
        ForeignKey("equipments.id"), primary_key=True
    )
    exercise_id: Mapped[UUID] = mapped_column(
        ForeignKey("exercises.id"), primary_key=True
    )

    # association between EquipmentExerciseRel -> Exercise
    exercise: Mapped["Exercise"] = relationship(back_populates="equipments_association")

    # association between EquipmentExerciseRel -> Equipment
    equipment: Mapped["Equipment"] = relationship(
        back_populates="exercises_association", lazy="joined"
    )


class MuscleExerciseRel(TimestampMixin, BaseTable):
    __tablename__ = "muscle_exercise_rel"
    muscle_id: Mapped[int] = mapped_column(ForeignKey("muscles.id"), primary_key=True)
    exercise_id: Mapped[UUID] = mapped_column(
        ForeignKey("exercises.id"), primary_key=True
    )
    procent: Mapped[int] = mapped_column(default=1)  # from 1 to 100
    type: Mapped[Enum] = mapped_column(Enum(MuscleEnum))

    # association between MuscleExerciseRel -> Exercise
    exercise: Mapped["Exercise"] = relationship(back_populates="muscles_association")

    # association between MuscleExerciseRel -> Muscle
    muscle: Mapped["Muscle"] = relationship(
        back_populates="exercises_association", lazy="joined"
    )
