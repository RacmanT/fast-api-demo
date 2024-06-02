import os

from pydantic_settings import BaseSettings, SettingsConfigDict


base_dir = os.path.abspath(os.path.join(__file__, "../../../"))
env_file_path = os.path.join(base_dir, "dotfiles", ".env")
env_file_path = (
    env_file_path
    if os.path.isfile(env_file_path)
    else os.path.join(base_dir, "dotfiles", ".env.default")
)


def get_env_file_path():
    base_dir = os.path.abspath(os.path.join(__file__, "../../../"))
    dotenv_path = os.path.join(base_dir, "dotfiles", ".env")
    default_env_path = os.path.join(base_dir, "dotfiles", ".env.default")
    return dotenv_path if os.path.isfile(dotenv_path) else default_env_path


class Settings(BaseSettings):
    postgres_db: str
    postgres_user: str
    postgres_password: str

    model_config = SettingsConfigDict(env_file=get_env_file_path())


settings = Settings()
