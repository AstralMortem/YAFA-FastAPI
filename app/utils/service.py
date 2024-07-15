from typing import Callable, Generic, TypeVar
from pydantic import BaseModel

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

    async def add(self, data: CREATE_MODEL, *args, **kwargs):
        instance = await self.repository.create(data.model_dump(), *args, **kwargs)
        return self.list_model.model_validate(instance)

    async def update(self, pk: PrimaryKey, data: UPDATE_MODEL, *args, **kwargs):
        instance = await self.repository.update(pk, data.model_dump(), *args, **kwargs)
        return self.read_model.model_validate(instance)

    async def get(self, pk: PrimaryKey, *args, **kwargs):
        instance = await self.repository.get(pk, *args, **kwargs)
        return self.read_model.model_validate(instance)

    async def filter(self, *args, **kwargs):
        instance = await self.repository.filter(*args, **kwargs)
        return [self.list_model.model_validate(obj) for obj in instance]

    async def delete(self, pk: PrimaryKey, *args, **kwargs):
        instance = await self.repository.delete(pk, *args, **kwargs)
        return self.read_model.model_validate(instance)
