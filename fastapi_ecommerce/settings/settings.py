from pathlib import Path
from typing import Literal

from pydantic import BaseSettings


class EnvironmentSettings(BaseSettings):
    name: Literal["test", "development", "production"] = "development"

    class Config:
        env_prefix = "environment_"


class DBSettings(BaseSettings):
    engine_string: str

    class Config:
        env_prefix = "db_"


class DevelopmentDBSettings(DBSettings):
    engine_string: str = "sqlite:///development.sqlite3?check_same_thread=False"


class TestDBSettings(DBSettings):
    engine_string: str = "sqlite:///test.sqlite3?check_same_thread=False"