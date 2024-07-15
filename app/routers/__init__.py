from fastapi import APIRouter
from .auth import router as auth_r

from .exercises import router as exercises_r

from .equipments import router as equipment_r

from .muscles import router as muscle_r

from .routines import router as routine_r


routers_list: list[APIRouter] = [auth_r, exercises_r, equipment_r, muscle_r, routine_r]
