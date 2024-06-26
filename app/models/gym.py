from sqlalchemy.orm import Mapped, mapped_column
from .mixins import CommonIntMixin, BaseTable
from ..schemas.gym import EquipmentRead, MuscleRead


class Equipment(CommonIntMixin, BaseTable):
    __tablename__ = "equipments"
    title: Mapped[str]
    image: Mapped[str | None] = mapped_column(default=None)

    READ_MODEL = EquipmentRead
    DETAIL_MODEL = EquipmentRead


class Muscle(CommonIntMixin, BaseTable):
    __tablename__ = "muscles"
    title: Mapped[str]
    image: Mapped[str | None] = mapped_column(default=None)

    READ_MODEL = MuscleRead
    DETAIL_MODEL = MuscleRead
