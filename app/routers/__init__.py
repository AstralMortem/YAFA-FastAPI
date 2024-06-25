from fastapi import APIRouter
from .auth import router as auth_r


routers_list: list[APIRouter] = [auth_r]
