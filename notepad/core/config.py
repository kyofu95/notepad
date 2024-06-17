from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    ENVIRONMENT: str

    CORS_ALLOW_CREDENTIALS: bool = True
    CORS_ALLOWED_ORIGINS: list[str] = ["*"]
    CORS_ALLOWED_METHODS: list[str] = ["*"]
    CORS_ALLOWED_HEADERS: list[str] = ["*"]

    model_config = SettingsConfigDict(env_prefix="notepad_")


settings = Settings()
