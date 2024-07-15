from ..models.routines import Routine
from ..schemas.routine_schema import (
    RoutineCreateDTO,
    RoutineListDTO,
    RoutineReadDTO,
    RoutineUpdateDTO,
)
from ..repository.routine_repository import RoutineRepository
from .mixin import BaseService


class RoutineService(
    BaseService[
        Routine,
        RoutineCreateDTO,
        RoutineUpdateDTO,
        RoutineListDTO,
        RoutineReadDTO,
    ]
):
    def __init__(self, repository: type[RoutineRepository]):
        self.repository = repository()
        self.list_dto = RoutineListDTO
        self.read_dto = RoutineReadDTO
