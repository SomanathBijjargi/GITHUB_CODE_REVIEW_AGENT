from pydantic_settings import BaseSettings

class Settings(BaseSettings):

    GITHUB_TOKEN: str
    GEMINI_API_KEY: str
    GITHUB_WEBHOOK_SECRET: str
    MONGO_URI: str
    DB_NAME: str

    class Config:
        env_file = ".env"

settings = Settings()