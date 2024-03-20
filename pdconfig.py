from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    TOKEN: str
    CHAT_ID: str


settings = Settings()