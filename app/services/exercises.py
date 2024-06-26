from uuid import UUID
from ..schemas.exercises import (
    ExerciseCreate,
    ExerciseRead,
    ExerciseSelect,
    ExerciseUpdate,
)
from ..utils.repositories import AbstractRepository


class ExercisesService:
    def __init__(self, repo: type[AbstractRepository]):
        self.repo = repo()

    async def add_exercise(self, data: ExerciseCreate):
        record = await self.repo.insert(data.model_dump())
        return {"id": record.id}

    async def get_exercises(self):
        records = await self.repo.get()
        return [ExerciseSelect.model_validate(model) for model in records]

    async def get_exercise(self, id: UUID):
        record = await self.repo.get_one(id)
        return ExerciseRead.model_validate(record)

    async def update_exercise(self, id: UUID, data: ExerciseUpdate):
        record = await self.repo.update(id, data.model_dump())
        return ExerciseRead.model_validate(record)

    async def delete_exercise(self, id: UUID):
        record = await self.repo.delete(id)
        return ExerciseRead.model_validate(record)
