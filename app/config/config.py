import os

from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    postgres_db: str
    postgres_user: str
    postgres_password: str

    model_config = SettingsConfigDict(
                                      env_file=f"{os.path.dirname(os.path.abspath(__file__))}/.env")


settings = Config()
print(settings.model_dump())
