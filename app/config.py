from functools import cached_property

from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    # app
    debug: bool = False
    title: str = "CarShopBackend microservice"
    description: str = "Microservice for CarShopBackend for storing and editing photos "
    environment: str | None = "DEV"

    # db
    postgres_dsn: str = "postgresql+asyncpg://admin:admin123@localhost:5432/carshopdb"
    postgres_echo: bool = False
    postgres_schema: str = "photoservice"
    
    # pydantic
    model_config = SettingsConfigDict(frozen=True, extra="allow", env_file=".env")

    @cached_property
    def log_level(self) -> str:
        return "DEBUG" if self.debug else "INFO"


config = Config()