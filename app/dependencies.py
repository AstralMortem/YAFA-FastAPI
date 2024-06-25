from typing import Annotated
from fastapi import Depends
from .services.auth import fastapi_users
from .models.auth import User

secured_route: Annotated[User, Depends()] = Depends(
    fastapi_users.current_user(active=True)
)
