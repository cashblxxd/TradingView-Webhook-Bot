from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    KEY: str
    TG_ENABLED: str
    TOKEN: str
    CHAT_ID: str


settings = Settings()