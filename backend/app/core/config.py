from dotenv import load_dotenv
import os

load_dotenv()  # Automatically loads .env file

class Settings:
    DATABASE_URL: str = os.getenv("DATABASE_URL")
    PROJECT_NAME: str = "Military Asset Management System"

settings = Settings()
