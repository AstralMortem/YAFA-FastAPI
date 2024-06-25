import logging
import sys
from fastapi import FastAPI
from .config import settings
from .routers import routers_list


logging.basicConfig(
    stream=sys.stdout, level=logging.DEBUG if settings.DEBUG else logging.INFO
)


app = FastAPI(title=settings.project_name)


for router in routers_list:
    app.include_router(router)
