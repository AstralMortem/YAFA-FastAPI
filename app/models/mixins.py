from datetime import datetime
from uuid import UUID, uuid4
from sqlalchemy import func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class BaseTable(DeclarativeBase): ...


class UUIDPrimaryKey:
    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4())


class IntPrimaryKey:
    id: Mapped[int] = mapped_column(primary_key=True)


class TimestampMixin:
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    updated_at: Mapped[datetime | None] = mapped_column(onupdate=func.now())


class TimestampBoolMixin(TimestampMixin):
    is_active: Mapped[bool] = mapped_column(default=True)


class CommonUUIDMixin(UUIDPrimaryKey, TimestampBoolMixin): ...


class CommonIntMixin(IntPrimaryKey, TimestampBoolMixin): ...
