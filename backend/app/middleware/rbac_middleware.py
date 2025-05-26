from fastapi import FastAPI, Request, status, Security
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from starlette.middleware import Middleware
from fastapi.security.api_key import APIKeyHeader
from datetime import datetime
import logging
import traceback

# Import project-specific modules
from app.api.api_router import api_router
from app.core.config import settings

# RBAC Middleware (safe fallback if debugging startup issues)
try:
    from app.middleware.rbac_middleware import RBACMiddleware
    ALLOWED_ROLES = ["admin", "manager"]
    middleware = [Middleware(RBACMiddleware, allowed_roles=ALLOWED_ROLES)]
except ImportError:
    middleware = []

# Logger setup
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("military-asset-management")

# Error Handlers
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    logger.error(f"Validation error: {exc.errors()}")
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={"detail": exc.errors(), "body": exc.body},
    )

async def global_exception_handler(request: Request, exc: Exception):
    logger.error(f"Unexpected error: {str(exc)}")
    logger.error(traceback.format_exc())
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={"detail": "Internal Server Error"},
    )

# --- THIS IS THE IMPORTANT ADDITION FOR THE "AUTHORIZE" BUTTON ---
api_key_header = APIKeyHeader(name="x-user-role", auto_error=False)

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    docs_url=settings.DOCS_URL,
    redoc_url=settings.REDOC_URL,
    middleware=middleware,
    exception_handlers={
        RequestValidationError: validation_exception_handler,
        Exception: global_exception_handler,
    },
    dependencies=[Security(api_key_header)]  # <- This line enables the "Authorize" button
)

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup_event():
    try:
        from app.core.db import Base, engine
        Base.metadata.create_all(bind=engine)
        await initialize_default_data()
        logger.info(f"✅ Server started successfully at {datetime.utcnow().isoformat()}")
        logger.info(f"Docs available at {settings.DOCS_URL}")
    except Exception as e:
        logger.error(f"Failed to start server: {str(e)}")
        logger.error(traceback.format_exc())
        raise

@app.on_event("shutdown")
async def shutdown_event():
    logger.info(f"🛑 Server shutdown at {datetime.utcnow().isoformat()}")

async def initialize_default_data():
    pass

# Mount API routers
app.include_router(
    api_router,
    prefix=settings.API_PREFIX,
    tags=["Military Assets"]
)

@app.get("/", include_in_schema=False)
async def root():
    return {
        "message": "Military Asset Management API",
        "version": settings.VERSION,
        "status": "operational",
        "timestamp": datetime.utcnow().isoformat(),
        "docs": settings.DOCS_URL,
        "redoc": settings.REDOC_URL
    }

@app.get("/health", tags=["System"])
async def health_check():
    return {
        "status": "healthy",
        "timestamp": datetime.utcnow().isoformat()
    }
