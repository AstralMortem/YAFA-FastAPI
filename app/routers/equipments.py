from typing import Annotated
from fastapi import APIRouter, Depends

from ..schemas.gym import EquipmentCreate, EquipmentUpdate, EquipmentRead
from ..dependencies import equipment_service


router = APIRouter(prefix="/equipments", tags=["Equipments"])


@router.get("")
async def gets_equipments(service=equipment_service) -> list[EquipmentRead]:
    return await service.gets_equipments()


@router.get("/{equipment_id}")
async def get_equipment(
    equipment_id: int, service=equipment_service
) -> EquipmentRead | None:
    return await service.get_equipment(equipment_id)


@router.post("")
async def add_equipment(
    data: Annotated[EquipmentCreate, Depends()], service=equipment_service
) -> EquipmentRead:
    return await service.add_equipment(data)


@router.patch("/{equipment_id}")
async def update_equipment(
    id: int, data: Annotated[EquipmentUpdate, Depends()], service=equipment_service
) -> EquipmentRead:
    return await service.update_equipment(id, data)


@router.delete("/{equipment_id}")
async def delete_equipment(id: int, service=equipment_service) -> EquipmentRead:
    return await service.delete_equipment(id)
