from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/assets")
def get_assets():
    return [
        {"id": 1, "name": "Tank A", "type": "Vehicle", "status": "Active"},
        {"id": 2, "name": "Drone X", "type": "UAV", "status": "Inactive"},
    ]
@app.get("/")
def read_root():
    return {"message": "FastAPI is running"}