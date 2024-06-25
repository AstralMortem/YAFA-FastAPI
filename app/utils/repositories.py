from abc import ABC, abstractmethod
from sqlalchemy import insert, select, update, delete
from uuid import UUID
from ..models.mixins import BaseTable
from ..database import sessionmanager

type PrimaryKey = str | int | UUID


class AbstractRepository(ABC):
    @abstractmethod
    async def insert(self, data):
        raise NotImplemented

    @abstractmethod
    async def get(self, filter=None):
        raise NotImplemented

    @abstractmethod
    async def get_one(self, id, _column=None):
        raise NotImplemented

    @abstractmethod
    async def update(self, id, data, _column=None):
        raise NotImplemented

    @abstractmethod
    async def delete(self, id, _column=None):
        raise NotImplemented

    @abstractmethod
    async def custom(self, statement, _commit=False):
        raise NotImplemented


class SQLAlchemyRepository(AbstractRepository):
    model: type[BaseTable]

    async def get_one(self, id: PrimaryKey, _column="id"):
        async with sessionmanager.session() as session:
            query = select(self.model).where(self.model.__dict__[_column] == id)
            result = await session.execute(query)
            return result.scalar_one_or_none()

    async def get(self, filter: tuple | None = None):
        async with sessionmanager.session() as session:
            query = select(self.model)
            if filter:
                query.filter(*filter)
            result = await session.execute(query)
            return result.scalars().all()

    async def insert(self, data: dict):
        async with sessionmanager.session() as session:
            query = insert(self.model).values(**data).returning(self.model)
            result = await session.execute(query)
            await session.commit()
            return result.scalar_one_or_none()

    async def update(self, id: PrimaryKey, data: dict, _column="id"):
        async with sessionmanager.session() as session:
            query = (
                update(self.model)
                .where(self.model.__dict__[_column] == id)
                .values(**data)
                .returning(self.model)
            )
            result = await session.execute(query)
            await session.commit()
            return result.scalar_one_or_none()

    async def delete(self, id: PrimaryKey, _column="id"):
        async with sessionmanager.session() as session:
            query = (
                delete(self.model)
                .where(self.model.__dict__[_column] == id)
                .returning(self.model)
            )
            result = await session.execute(query)
            await session.commit()
            return result.scalar_one_or_none()

    async def custom(self, statement, _commit=False):
        async with sessionmanager.session() as session:
            result = await session.execute(statement)
            if _commit:
                await session.commit()
            return result
