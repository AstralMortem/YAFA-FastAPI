from ..schemas.exercises import ExerciseCreate
from ..utils.service import SimpleCRUDService


class ExerciseService(SimpleCRUDService):
    def __init__(self, *args, **kwargs):
        super(ExerciseService, self).__init__(*args, **kwargs)

    async def add_exercise(self, data: ExerciseCreate):
        record = await self.add(data)
        return {"id": record.id}


class EquipmentService(SimpleCRUDService):
    def __init__(self, *args, **kwargs):
        super(EquipmentService, self).__init__(*args, **kwargs)


class MuscleService(SimpleCRUDService):
    def __init__(self, *args, **kwargs):
        super(MuscleService, self).__init__(*args, **kwargs)
