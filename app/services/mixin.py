from abc import ABC, abstractmethod
from typing import Generic, TypeVar
from pydantic import BaseModel
from ..repository.mixin import (
    _ORM_MODEL,
    AbstractRepository,
    PrimaryKey,
    SQLAlchemyRepository,
)

_DTO_CREATE = TypeVar("_DTO_CREATE", bound=BaseModel)
_DTO_UPDATE = TypeVar("_DTO_UPDATE", bound=BaseModel)
_DTO_READ = TypeVar("_DTO_READ", bound=BaseModel)
_DTO_LIST = TypeVar("_DTO_LIST", bound=BaseModel)


class AbstractService(ABC):
    @abstractmethod
    def __init__(self, repository: type[AbstractRepository]):
        raise NotImplemented

    @abstractmethod
    async def get_item(self, pk: PrimaryKey):
        raise NotImplemented

    @abstractmethod
    async def get_items(self):
        raise NotImplemented

    @abstractmethod
    async def create_item(self, data: BaseModel):
        raise NotImplemented

    @abstractmethod
    async def update_item(self, pk: PrimaryKey, data: BaseModel):
        raise NotImplemented

    @abstractmethod
    async def delete_item(self, pk: PrimaryKey):
        raise NotImplemented


class BaseService(
    Generic[_ORM_MODEL, _DTO_CREATE, _DTO_UPDATE, _DTO_LIST, _DTO_READ], AbstractService
):
    def __init__(
        self,
        repository: type[SQLAlchemyRepository[_ORM_MODEL]],
    ):
        self.repository = repository()
        self.list_dto: type[_DTO_LIST]
        self.read_dto: type[_DTO_READ]

    async def get_item(self, pk: PrimaryKey):
        instance = await self.repository.get(pk)
        return self.read_dto.model_validate(instance)

    async def get_items(self):
        instance = await self.repository.filter(None, None)
        return [self.list_dto.model_validate(row) for row in instance]

    async def create_item(self, data: _DTO_CREATE):
        instance = await self.repository.create(data.model_dump())
        return self.list_dto.model_validate(instance)

    async def update_item(self, pk: PrimaryKey, data: _DTO_UPDATE):
        instance = await self.repository.update(pk, data.model_dump())
        return self.read_dto.model_validate(instance)

    async def delete_item(self, pk: PrimaryKey):
        instance = await self.repository.delete(pk)
        return self.read_dto.model_validate(instance)
