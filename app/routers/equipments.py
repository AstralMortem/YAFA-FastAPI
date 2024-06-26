from typing import Annotated
from fastapi import APIRouter, Depends

from ..schemas.gym import EquipmentCreate, EquipmentUpdate
from ..dependencies import equipment_service


router = APIRouter(prefix="/equipments", tags=["Equipments"])


@router.get("")
async def get_all_equipments(service: equipment_service):
    return await service.filter()


@router.get("/{equipment_id}")
async def get_equipment_by_id(equipment_id: int, service: equipment_service):
    return await service.get(equipment_id)


@router.post("")
async def add_equipment(
    data: Annotated[EquipmentCreate, Depends()], service: equipment_service
):
    return await service.add(data)


@router.patch("/{equipment_id}")
async def update_equipment(
    equipment_id: int,
    data: Annotated[EquipmentUpdate, Depends()],
    service: equipment_service,
):
    return await service.update(equipment_id, data)


@router.delete("/{equipment_id}")
async def delete_equipment(equipment_id: int, service: equipment_service):
    return await service.delete(equipment_id)
