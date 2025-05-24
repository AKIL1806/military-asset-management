from dotenv import load_dotenv
import os

load_dotenv()  # Load from .env file at root or backend folder

class Settings:
    PROJECT_NAME: str = "Military Asset Management System"
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./dev.db")  # fallback to sqlite
    SECRET_KEY: str = os.getenv("SECRET_KEY", "your-secret-key")

settings = Settings()
