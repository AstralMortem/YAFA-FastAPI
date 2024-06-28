from typing import TYPE_CHECKING
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .mixins import CommonIntMixin, BaseTable

if TYPE_CHECKING:
    from .exercises import MuscleExerciseRel, Exercise


class Equipment(CommonIntMixin, BaseTable):
    __tablename__ = "equipments"
    title: Mapped[str]
    image: Mapped[str | None] = mapped_column(default=None)

    exercises: Mapped[list["Exercise"]] = relationship(
        secondary="equipment_exercise_rel", back_populates="equipments"
    )


class Muscle(CommonIntMixin, BaseTable):
    __tablename__ = "muscles"
    title: Mapped[str]
    image: Mapped[str | None] = mapped_column(default=None)

    # association between Muscle -> MuscleExerciseRel -> Exercise
    exercise_details: Mapped[list["MuscleExerciseRel"]] = relationship(
        back_populates="muscle"
    )
