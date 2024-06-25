from fastapi import APIRouter
from ..services.auth import fastapi_users, auth_backend
from ..schemas.auth import UserCreate, UserRead, UserUpdate
from ..config import settings
from ..utils.oauth import google_oauth_client

router = APIRouter(prefix="/auth", tags=["Auth"])


router.include_router(fastapi_users.get_auth_router(auth_backend), prefix="/jwt")
router.include_router(fastapi_users.get_register_router(UserRead, UserCreate))
router.include_router(fastapi_users.get_reset_password_router())
router.include_router(fastapi_users.get_verify_router(UserRead))
router.include_router(fastapi_users.get_users_router(UserRead, UserUpdate))
router.include_router(
    fastapi_users.get_oauth_router(
        google_oauth_client,
        auth_backend,
        settings.SECRET_KEY,
        associate_by_email=True,
        is_verified_by_default=True,
    ),
    tags=["OAuth"],
    prefix="/google",
)
