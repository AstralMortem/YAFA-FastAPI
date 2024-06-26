from sqlalchemy.orm import Mapped, mapped_column, relationship
from .mixins import CommonIntMixin, BaseTable


class Equipment(CommonIntMixin, BaseTable):
    __tablename__ = "equipments"
    title: Mapped[str]
    image: Mapped[str | None] = mapped_column(default=None)


class Muscle(CommonIntMixin, BaseTable):
    __tablename__ = "muscles"
    title: Mapped[str]
    image: Mapped[str | None] = mapped_column(default=None)
