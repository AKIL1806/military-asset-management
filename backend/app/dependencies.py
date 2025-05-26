# backend/app/dependencies.py

from fastapi.security.api_key import APIKeyHeader
from fastapi import Security

api_key_header = APIKeyHeader(name="x-user-role", auto_error=False)

def get_user_role(x_user_role: str = Security(api_key_header)):
    return x_user_role
