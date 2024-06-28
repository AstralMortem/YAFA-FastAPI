from abc import ABC, abstractmethod
from typing import Any, Generic, Optional, Tuple, TypeVar
from uuid import UUID

from pydantic import BaseModel
from sqlalchemy import BinaryExpression, insert, select, update
from sqlalchemy.sql.base import ExecutableOption

from ..exceptions import ModelDoesNotExists
from ..models.mixins import BaseTable
from ..database import sessionmanager

_ORM_MODEL = TypeVar("_ORM_MODEL", bound=BaseTable)
_DTO_CREATE = TypeVar("_DTO_CREATE", bound=BaseModel)
_DTO_UPDATE = TypeVar("_DTO_UPDATE", bound=BaseModel)
_DTO_READ = TypeVar("_DTO_READ", bound=BaseModel)
_DTO_LIST = TypeVar("_DTO_LIST", bound=BaseModel)

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
    async def create(self, data: BaseModel):
        raise NotImplemented

    @abstractmethod
    async def update(self, pk, data: BaseModel):
        raise NotImplemented

    @abstractmethod
    async def delete(self, pk: PrimaryKey):
        raise NotImplemented


class SQLAlchemyRepository(
    Generic[_ORM_MODEL, _DTO_CREATE, _DTO_UPDATE, _DTO_LIST, _DTO_READ],
    AbstractRepository,
):
    model: type[_ORM_MODEL]
    dto_list_model: type[_DTO_LIST]
    dto_read_model: type[_DTO_READ]
    # dto_update_model: type[_DTO_UPDATE]
    # dto_create_model: type[_DTO_CREATE]

    async def get(self, pk: str | int | UUID):
        async with sessionmanager.session() as session:
            instance = await session.get(self.model, pk)
            if not instance:
                raise ModelDoesNotExists(self.model)
            return self.dto_read_model.model_validate(instance)

    async def filter(
        self,
        conditions: Optional[Tuple[BinaryExpression]],
        options: Optional[Tuple[ExecutableOption]],
    ):
        async with sessionmanager.session() as session:
            q = select(self.model)
            if conditions:
                q = q.where(*conditions)
            if options:
                q = q.options(*options)

            instance = await session.scalars(q)
            return [self.dto_list_model.model_validate(obj) for obj in instance]

    async def create(self, data: _DTO_CREATE):
        async with sessionmanager.session() as session:
            instance = self.model(**data.model_dump())
            session.add(instance)
            await session.commit()
            await session.refresh(instance)
            return self.dto_list_model.model_validate(instance)

    async def update(self, pk: str | int | UUID, data: _DTO_UPDATE):
        async with sessionmanager.session() as session:
            q = update(self.model).where(self.model.id == pk).values(**data.model_dump()).returning(self.model)  # type: ignore
            instance = await session.scalar(q)
            if not instance:
                raise ModelDoesNotExists(self.model)
            return self.dto_read_model.model_validate(instance)

    async def delete(self, pk: str | int | UUID):
        async with sessionmanager.session() as session:
            instance = await self.get(pk)
            await session.delete(instance)
            await session.commit()
            return instance
