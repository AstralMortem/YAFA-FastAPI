from ..utils.service import BaseCRUDService
from ..schemas.gym import (
    EquipmentCreate,
    EquipmentRead,
    EquipmentUpdate,
    MuscleCreate,
    MuscleRead,
    MuscleUpdate,
)


class EquipmentService(
    BaseCRUDService[EquipmentCreate, EquipmentUpdate, EquipmentRead, EquipmentRead]
):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.read_model = EquipmentRead
        self.list_model = EquipmentRead


class MuscleService(
    BaseCRUDService[MuscleCreate, MuscleUpdate, MuscleRead, MuscleRead]
):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.read_model = MuscleRead
        self.list_model = MuscleRead
