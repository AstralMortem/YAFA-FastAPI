from uuid import UUID
from sqlalchemy import Enum, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from .mixins import BaseTable, CommonUUIDMixin
from ..utils.enums import ExerciseTypeEnum


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
