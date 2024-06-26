from typing import Generic, TypeVar
from uuid import UUID
from sqlalchemy import BinaryExpression, select, update
from ..database import sessionmanager
from ..models.mixins import BaseTable

Model = TypeVar("Model", bound=BaseTable)
type PrimaryKey = str | int | UUID


class SQLAlchemyRepository(Generic[Model]):
    def __init__(self, model: type[Model]):
        self.model = model

    async def create(self, data: dict):
        async with sessionmanager.session() as session:
            instance = self.model(**data)
            session.add(instance)
            await session.commit()
            await session.refresh(instance)
            return instance

    async def get(self, pk: PrimaryKey):
        async with sessionmanager.session() as session:
            instance = await session.get(self.model, pk)
            if not instance:
                raise Exception(f"{self.model} does not exist")
            return instance

    async def filter(self, join=None, *expressions: BinaryExpression):
        async with sessionmanager.session() as session:
            query = select(self.model)
            if join:
                query = query.join(join)
            if expressions:
                query = query.where(*expressions)
            return list(await session.scalars(query))

    async def delete(self, pk: PrimaryKey):
        async with sessionmanager.session() as session:
            instance = await self.get(pk)
            await session.delete(instance)
            await session.commit()
            return instance

    async def update(self, pk: PrimaryKey, data: dict):
        async with sessionmanager.session() as session:
            query = (
                update(self.model)
                .where(self.model.id == pk)
                .values(**data)
                .returning(self.model)
            )
            result = await session.execute(query)
            return result.scalar_one()
