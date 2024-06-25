from typing import List
from fastapi_users.db import (
    SQLAlchemyBaseUserTableUUID,
    SQLAlchemyBaseOAuthAccountTableUUID,
)
from sqlalchemy.orm import Mapped, relationship
from .mixins import BaseTable


class OAuthAccount(SQLAlchemyBaseOAuthAccountTableUUID, BaseTable):
    pass


class User(SQLAlchemyBaseUserTableUUID, BaseTable):
    oauth_accounts: Mapped[List[OAuthAccount]] = relationship(
        "OAuthAccount", lazy="joined"
    )
