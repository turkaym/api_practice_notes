import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    APP_NAME: str = os.getenv("APP_NAME", "FastAPI App")
    ENV: str = os.getenv("ENV", "environment")
    DEBUG: bool = os.getenv("DEBUG", "false").lower() == "true"

    DATABASE_URL: str = os.getenv("DATABASE_URL")

    JWT_SECRET: str = os.getenv("JWT_SECRET")


settings = Settings()
