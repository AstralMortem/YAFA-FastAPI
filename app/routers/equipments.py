from typing import Annotated
from fastapi import APIRouter, Depends

from ..schemas.equipment_schema import EquipmentCreateDTO, EquipmentUpdateDTO
from ..dependencies import equipment_service


router = APIRouter(prefix="/equipments", tags=["Equipments"])


@router.get("")
async def get_equipments(service: equipment_service):
    return await service.get_items()


@router.get("/{equipment_id}")
async def get_equipment_by_id(equipment_id: int, service: equipment_service):
    return await service.get_item(equipment_id)


@router.post("")
async def add_equipment(
    data: Annotated[EquipmentCreateDTO, Depends()], service: equipment_service
):
    return await service.create_item(data)


@router.patch("/{equipment_id}")
async def update_equipment(
    equipment_id: int,
    data: Annotated[EquipmentUpdateDTO, Depends()],
    service: equipment_service,
):
    return await service.update_item(equipment_id, data)


@router.delete("/{equipment_id}")
async def delete_equipment(equipment_id: int, service: equipment_service):
    return await service.delete_item(equipment_id)
