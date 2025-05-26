from dotenv import load_dotenv
import os

load_dotenv()  # Automatically loads .env file

class Settings:
    PROJECT_NAME = "Military Asset Management"
    VERSION = "1.0.0"
    API_PREFIX = "/api/v1"
    BACKEND_CORS_ORIGINS = ["*"]
    LOGGER_NAME = "military_api"
    LOG_LEVEL = "INFO"
    DOCS_URL = "/docs"
    REDOC_URL = "/redoc"

settings = Settings()
