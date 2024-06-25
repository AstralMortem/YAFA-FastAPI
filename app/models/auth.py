from typing import List
from fastapi_users.db import (
    SQLAlchemyBaseUserTableUUID,
    SQLAlchemyBaseOAuthAccountTableUUID,
)
from sqlalchemy import Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .mixins import BaseTable, TimestampMixin
from ..utils.enums import GenderEnum, TrainingAimEnum


class OAuthAccount(SQLAlchemyBaseOAuthAccountTableUUID, BaseTable):
    pass


class User(SQLAlchemyBaseUserTableUUID, TimestampMixin, BaseTable):
    full_name: Mapped[str]
    age: Mapped[int]
    gender: Mapped[Enum] = mapped_column(Enum(GenderEnum))
    height: Mapped[int]
    weight: Mapped[int]
    training_time: Mapped[int] = mapped_column(default=2700)  # in seconds
    rest_time: Mapped[int] = mapped_column(default=60)  # in seconds
    training_per_week: Mapped[int]
    training_aim: Mapped[Enum] = mapped_column(Enum(TrainingAimEnum))
    oauth_accounts: Mapped[List[OAuthAccount]] = relationship(
        "OAuthAccount", lazy="joined"
    )
