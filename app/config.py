# app/config.py
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    DATABASE_URL: str

    # Permite inyectar variables declaradas dentro de un archivo local .env
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

settings = Settings()