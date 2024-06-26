from fastapi import APIRouter
from .auth import router as auth_r
from .exercises import router as exercises_r


routers_list: list[APIRouter] = [auth_r, exercises_r]
