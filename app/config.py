import os
from pathlib import Path
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # PATH SETTINGS
    PROJECT_DIR: Path = Path.cwd()
    BASE_DIR: Path = PROJECT_DIR.joinpath("src")
    MODULES_DIR: Path = BASE_DIR.joinpath("modules")

    # DATABASE SETTINGS
    DB_HOST: str = os.getenv("DB_HOST", "localhost")
    DB_PORT: int = int(os.getenv("DB_PORT", 5432))
    DB_NAME: str = os.getenv("DB_NAME", "fitness")
    DB_USER: str = os.getenv("DB_USER", "fitness")
    DB_PASS: str = os.getenv("DB_PASS", "fitness")
    DB_ECHO: bool = True

    db_path: str = f"{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    sync_db_path: str = f"postgresql+psycopg2://{db_path}"
    async_db_path: str = f"postgresql+asyncpg://{db_path}"

    # PROJECT SETTINGS
    DEBUG: bool = True  # change on production
    project_name: str = "Fitness App"

    # SECURE SETTINGS
    SECRET_KEY: str = os.getenv(
        "SECRET_KEY", "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
    )

    # OAUTH
    GOOGLE_CLIENT_ID: str = os.getenv("GOOGLE_CLIENT_ID", "")
    GOOGLE_SECRET_KEY: str = os.getenv("GOOGLE_SECRET_KEY", "")


settings = Settings()
