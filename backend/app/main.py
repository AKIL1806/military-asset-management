from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import assets  # Import the assets router

app = FastAPI()

# Allow frontend dev server to access backend
origins = [
    "http://localhost:5173",
]

# Enable CORS for frontend-backend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount assets router under /api/assets
app.include_router(assets.router, prefix="/api/assets", tags=["assets"])

# Health check route
@app.get("/")
async def root():
    return {"message": "FastAPI is running"}
