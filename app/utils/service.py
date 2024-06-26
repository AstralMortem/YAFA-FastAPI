from typing import Any, Callable
from .repositories import AbstractRepository, PrimaryKey, SQLAlchemyRepository
from pydantic import BaseModel


class SimpleCRUDService(object):
    repo: AbstractRepository

    def __init__(self, repository: type[AbstractRepository]):
        self.repo = repository()

    def __getattribute__(self, name: str):
        keys = ["add", "gets", "get", "update", "delete"]
        print(name)
        for key in keys:
            if name.startswith(key):
                return super().__getattribute__(key)
        return super().__getattribute__(name)

    async def add(self, data: BaseModel):
        return await self.repo.insert(data.model_dump())

    async def gets(self, *args):
        return await self.repo.get(*args)

    async def get(self, id: PrimaryKey, *args):
        return await self.repo.get_one(id, *args)

    async def update(self, id: PrimaryKey, data: BaseModel, *args):
        return await self.repo.update(id, data.model_dump(), *args)

    async def delete(self, id: PrimaryKey, *args):
        return await self.repo.delete(id, *args)
