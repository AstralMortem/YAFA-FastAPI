from app import repository
from .repository.muscle_repository import MuscleRepository
from .services.muscle_service import MuscleService
from .repository.mixin import (
    _DTO_CREATE,
    _DTO_LIST,
    _DTO_READ,
    _DTO_UPDATE,
    _ORM_MODEL,
    SQLAlchemyRepository,
)
from .repository.equipment_repository import EquipmentRepository
from .services.equipment_service import EquipmentService
from .services.auth import fastapi_users
from typing import Annotated
from fastapi import Depends
from .models.auth import User


secured_route: Annotated[User, Depends()] = Depends(
    fastapi_users.current_user(active=True)
)


def get_equipment_service():
    return EquipmentService(EquipmentRepository)


equipment_service = Annotated[EquipmentService, Depends(get_equipment_service)]


def get_muscle_service():
    return MuscleService(MuscleRepository)


muscle_service = Annotated[MuscleService, Depends(get_muscle_service)]
