"""
    Application Settings
"""
import os

DATABASE_URL = os.environ.get("DATABASE_URL", "postgresql+asyncpg://viya:viya123@viya.postgres:5432/viya")
