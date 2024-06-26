from ..utils.service import BaseCRUDService
from ..schemas.exercises import (
    ExerciseCreate,
    ExerciseRead,
    ExerciseList,
    ExerciseUpdate,
)


class ExerciseService(
    BaseCRUDService[ExerciseCreate, ExerciseUpdate, ExerciseRead, ExerciseList]
):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.read_model = ExerciseRead
        self.list_model = ExerciseList
