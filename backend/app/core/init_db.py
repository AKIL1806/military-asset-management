from app.core.db import engine, Base
from app.models import Asset  # This imports all your models

def init_db():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    init_db()
    print("Database tables created successfully")