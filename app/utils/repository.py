from typing import Generic, TypeVar, Tuple
from uuid import UUID
from sqlalchemy import BinaryExpression, Result, select, update
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import session
from sqlalchemy.sql.base import ExecutableOption
from sqlalchemy.sql.selectable import TypedReturnsRows, _T
from ..models.mixins import BaseTable

Model = TypeVar("Model", bound=BaseTable)
type PrimaryKey = str | int | UUID


class SQLAlchemyRepository(Generic[Model]):
    def __init__(self, model: type[Model], session: AsyncSession):
        self.model = model
        self.session = session

    async def create(self, data: dict):
        instance = self.model(**data)
        self.session.add(instance)
        await self.session.commit()
        await self.session.refresh(instance)
        return instance

    async def get(self, pk: PrimaryKey):
        instance = await self.session.get(self.model, pk)
        if not instance:
            raise Exception(f"{self.model} does not exist")
        return instance

    async def filter(
        self,
        expressions: Tuple[BinaryExpression] | None = None,
        options: Tuple[ExecutableOption] | ExecutableOption | None = None,
    ):
        query = select(self.model)
        if isinstance(expressions, Tuple):
            query = query.where(*expressions)
        if options:
            if isinstance(options, Tuple):
                query = query.options(*options)
            else:
                query = query.options(options)
        return list(await self.session.scalars(query))

    async def delete(self, pk: PrimaryKey):
        instance = await self.get(pk)
        await self.session.delete(instance)
        await self.session.commit()
        return instance

    async def update(self, pk: PrimaryKey, data: dict):
        query = (
            update(self.model)
            .where(self.model.id == pk)
            .values(**data)
            .returning(self.model)
        )
        result = await self.session.execute(query)
        return result.scalar_one()

    async def custom(self, statement: TypedReturnsRows[_T]) -> Result[_T]:
        return await self.session.execute(statement)

    async def custom_commit(self, statement: TypedReturnsRows[_T]) -> Result[_T]:
        something = await self.session.execute(statement)
        await self.session.commit()
        return something
