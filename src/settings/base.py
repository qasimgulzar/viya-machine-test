"""
    Application Settings
"""
import os

DATABASE_URL = os.environ.get("DATABASE_URL", "postgresql+asyncpg://viya:viya123@viya.postgres:5432/viya")
CORS_ALLOWED_ORIGINS = ["*"]
CORS_ALLOWED_METHODS = ["*"]
CORS_ALLOWED_HEADERS = ["*"]
CORS_ALLOW_CREDENTIALS = True
