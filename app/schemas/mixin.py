from datetime import datetime


class TimeStampDTOMixin:
    created_at: datetime
    updated_at: datetime | None = None


class ActiveDTOMixin:
    is_active: bool = True


class CommonDTOMixin(TimeStampDTOMixin, ActiveDTOMixin): ...
