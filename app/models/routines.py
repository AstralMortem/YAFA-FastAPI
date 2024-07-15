from typing import TYPE_CHECKING
from uuid import UUID
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .mixins import CommonUUIDMixin, BaseTable, TimestampMixin

if TYPE_CHECKING:
    from .exercises import Exercise


class Routine(CommonUUIDMixin, BaseTable):
    __tablename__ = "routines"
    title: Mapped[str]
    is_public: Mapped[bool] = mapped_column(default=True)
    author_id: Mapped[UUID | None] = mapped_column(ForeignKey("user.id"), default=None)

    # relation between  Routine -> ExercieRoutineRel
    exercise_association: Mapped[list["ExerciseRoutineRel"]] = relationship(
        back_populates="routine",
        cascade="save-update, merge, delete, delete-orphan",
        lazy="selectin",
    )


class ExerciseRoutineRel(TimestampMixin, BaseTable):
    __tablename__ = "exercise_routine_rel"
    exercise_id: Mapped[UUID] = mapped_column(
        ForeignKey("exercises.id"), primary_key=True
    )
    routine_id: Mapped[UUID] = mapped_column(
        ForeignKey("routines.id"), primary_key=True
    )
    sets: Mapped[int] = mapped_column(default=3)
    reps: Mapped[int] = mapped_column(default=10)  # can be time in seconds
    reps_is_time: Mapped[bool] = mapped_column(default=False)

    # relation between  ExercieRoutineRel -> Routine
    routine: Mapped["Routine"] = relationship(back_populates="exercise_association")

    # relation between ExercieRoutineRel -> Exercise
    exercise: Mapped["Exercise"] = relationship(
        back_populates="routine_association", lazy="joined"
    )
