from abc import ABC, abstractmethod
from typing import Any, Generic, Optional, Tuple, TypeVar
from uuid import UUID
from sqlalchemy import BinaryExpression, select
from sqlalchemy.orm.interfaces import ORMOption
from sqlalchemy.sql.base import ExecutableOption

from ..exceptions import ModelDoesNotExists
from ..models.mixins import BaseTable
from ..database import sessionmanager

_ORM_MODEL = TypeVar("_ORM_MODEL", bound=BaseTable)


type PrimaryKey = str | int | UUID


class AbstractRepository(ABC):

    @abstractmethod
    async def get(self, pk: PrimaryKey):
        raise NotImplemented

    @abstractmethod
    async def filter(
        self,
        conditions: Optional[Tuple[BinaryExpression]],
        options: Optional[Tuple[ExecutableOption]],
    ):
        raise NotImplemented

    @abstractmethod
    async def create(self, data: dict[str, Any]):
        raise NotImplemented

    @abstractmethod
    async def update(self, pk, data: dict[str, Any]):
        raise NotImplemented

    @abstractmethod
    async def delete(self, pk: PrimaryKey):
        raise NotImplemented

    @abstractmethod
    async def custom(self, statement):
        raise NotImplemented


class SQLAlchemyRepository(
    Generic[_ORM_MODEL],
    AbstractRepository,
):
    model: type[_ORM_MODEL]

    async def get(
        self, pk: str | int | UUID, options: Optional[Tuple[ORMOption]] = None
    ):
        async with sessionmanager.session() as session:
            instance = await session.get(self.model, pk, options=options)
            if not instance:
                raise ModelDoesNotExists(self.model)
            return instance

    async def filter(
        self,
        conditions: Optional[Tuple[BinaryExpression]],
        options: Optional[Tuple[ExecutableOption]],
    ):
        async with sessionmanager.session() as session:
            q = select(self.model)
            if conditions is not None:
                q = q.where(*conditions)
            if options:
                q = q.options(*options)

            instance = await session.scalars(q)
            return list(instance)

    async def create(self, data: dict[str, Any]):
        async with sessionmanager.session() as session:
            instance = self.model(**data)
            session.add(instance)
            await session.commit()
            await session.refresh(instance)
            return instance

    async def update(self, pk: str | int | UUID, data: dict[str, Any]):
        async with sessionmanager.session() as session:
            instance = await self.get(pk)
            for key, val in data:
                setattr(instance, key, val)
            await session.commit()
            return instance

    async def delete(self, pk: str | int | UUID):
        async with sessionmanager.session() as session:
            instance = await self.get(pk)
            await session.delete(instance)
            await session.commit()
            return instance

    async def custom(self, statement):
        async with sessionmanager.session() as session:
            return await session.execute(statement)
