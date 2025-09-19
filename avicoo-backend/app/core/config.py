# app/core/config.py
from pydantic_settings import BaseSettings
from typing import List
import os

class Settings(BaseSettings):
    # Base
    app_name: str = "Avicoo API"
    app_version: str = "1.0.0"
    debug: bool = False
    
    # Database
    database_url: str = "postgresql+psycopg://avicoo:avicoo@db:5432/avicoo"
    
    # Security
    secret_key: str = "change_me_secret_key_here"
    access_token_expire_minutes: int = 1440
    
    # CORS
    cors_origins: List[str] = [
        "http://localhost:5173",
        "http://localhost:8080"
    ]
    
    # Business rules
    min_delivery_quantity: int = 5
    delivery_fee: int = 1000  # FCFA
    
    class Config:
        env_file = ".env"
        case_sensitive = False

settings = Settings()