from typing import Generic, TypeVar, Tuple
from uuid import UUID
from sqlalchemy import BinaryExpression, Executable, Result, select, update
from sqlalchemy.sql.base import ExecutableOption
from sqlalchemy.sql.selectable import TypedReturnsRows, _T
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

    async def filter(
        self,
        expressions: Tuple[BinaryExpression] | None = None,
        options: Tuple[ExecutableOption] | ExecutableOption | None = None,
    ):
        async with sessionmanager.session() as session:
            query = select(self.model)
            if isinstance(expressions, Tuple):
                query = query.where(*expressions)
            if options:
                if isinstance(options, Tuple):
                    query = query.options(*options)
                else:
                    query = query.options(options)
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

    async def custom(self, statement: TypedReturnsRows[_T]) -> Result[_T]:
        async with sessionmanager.session() as session:
            return await session.execute(statement)
