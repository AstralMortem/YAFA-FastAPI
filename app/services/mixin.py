from abc import ABC, abstractmethod
from typing import Generic
from pydantic import BaseModel
from ..repository.mixin import (
    _DTO_CREATE,
    _DTO_LIST,
    _DTO_READ,
    _DTO_UPDATE,
    _ORM_MODEL,
    AbstractRepository,
    PrimaryKey,
    SQLAlchemyRepository,
)


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
        repository: type[
            SQLAlchemyRepository[
                _ORM_MODEL, _DTO_CREATE, _DTO_UPDATE, _DTO_LIST, _DTO_READ
            ]
        ],
    ):
        self.repository = repository()

    async def get_item(self, pk: PrimaryKey):
        return await self.repository.get(pk)

    async def get_items(self):
        return await self.repository.filter(None, None)

    async def create_item(self, data: _DTO_CREATE):
        return await self.repository.create(data)

    async def update_item(self, pk: PrimaryKey, data: _DTO_UPDATE):
        return await self.repository.update(pk, data)

    async def delete_item(self, pk: PrimaryKey):
        return await self.repository.delete(pk)
