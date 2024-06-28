from typing import TYPE_CHECKING
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .mixins import CommonIntMixin, BaseTable

if TYPE_CHECKING:
    from .exercises import MuscleExerciseRel, EquipmentExerciseRel


class Equipment(CommonIntMixin, BaseTable):
    __tablename__ = "equipments"
    title: Mapped[str]
    image: Mapped[str | None] = mapped_column(default=None)
    exercises_association: Mapped[list["EquipmentExerciseRel"]] = relationship(
        back_populates="equipment"
    )


class Muscle(CommonIntMixin, BaseTable):
    __tablename__ = "muscles"
    title: Mapped[str]
    image: Mapped[str | None] = mapped_column(default=None)
    exercises_association: Mapped[list["MuscleExerciseRel"]] = relationship(
        back_populates="muscle"
    )
