from functools import cached_property

from pydantic import HttpUrl, PostgresDsn, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    # app
    debug: bool = False
    title: str = "backend-pet"
    description: str = "Something useful"
    environment: str | None = "DEV"
    photo_base_url: str = "http://localhost:8000"

    # db
    postgres_dsn: str = "postgresql+asyncpg://admin:admin123@localhost:5432/carshopdb"
    postgres_echo: bool = False
    postgres_schema: str = "photoservice"

    # sentry
    sentry_dsn: HttpUrl | None = None

    # client
    e1_endpoint: str = "http://e1-api.ua"
    e1_token: str = "backend_pet_test"

    # pydantic
    model_config = SettingsConfigDict(frozen=True, extra="allow", env_file=".env")

    @cached_property
    def log_level(self) -> str:
        return "DEBUG" if self.debug else "INFO"


config = Config()