from typing import Any
from ..models.mixins import BaseTable


def alchemy_row_2_dict(row: BaseTable):
    d = {}
    for column in row.__table__.columns:
        d[column.name] = getattr(row, column.name)
    return d


def replace_column_in_dict(row: BaseTable, column: str, value: Any):
    d = alchemy_row_2_dict(row)
    d[column] = value
    return d
