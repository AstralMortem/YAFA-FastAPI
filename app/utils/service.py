from ast import Call
from typing import Any, Callable, Generic, Self, TypeVar
from pydantic import BaseModel
from sqlalchemy import BinaryExpression

from .repository import PrimaryKey, SQLAlchemyRepository, Model

CREATE_MODEL = TypeVar("CREATE_MODEL", bound=BaseModel)
UPDATE_MODEL = TypeVar("UPDATE_MODEL", bound=BaseModel)
READ_MODEL = TypeVar("READ_MODEL", bound=BaseModel)
LIST_MODEL = TypeVar("LIST_MODEL", bound=BaseModel)


class BaseCRUDService(Generic[CREATE_MODEL, UPDATE_MODEL, READ_MODEL, LIST_MODEL]):
    def __init__(self, repository: Callable[[], SQLAlchemyRepository[Model]]):
        self.repository: SQLAlchemyRepository[Model] = repository()
        self.read_model: type[READ_MODEL]
        self.list_model: type[LIST_MODEL]

    async def add(self, data: CREATE_MODEL):
        instance = await self.repository.create(data.model_dump())
        return self.list_model.model_validate(instance)

    async def update(self, pk: PrimaryKey, data: UPDATE_MODEL):
        instance = await self.repository.update(pk, data.model_dump())
        return self.read_model.model_validate(instance)

    async def get(self, pk: PrimaryKey):
        instance = await self.repository.get(pk)
        return self.read_model.model_validate(instance)

    async def filter(self, join=None, *filter: BinaryExpression):
        instance = await self.repository.filter(join, *filter)
        return [self.list_model.model_validate(obj) for obj in instance]

    async def delete(self, pk: PrimaryKey):
        instance = await self.repository.delete(pk)
        return self.read_model.model_validate(instance)
