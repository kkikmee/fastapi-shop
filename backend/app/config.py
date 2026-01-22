from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "FastApi shop"
    debug: bool = True
    database_url: str = "sqlite:///./shop.db"
    cors_origins: list = [
        "hhtp://localhost:5173",
        "hhtp://localhost:3000",
        "hhtp://127.0.0.1:5173",
        "hhtp://127.0.0.1:3000",
    ]
    static_dir: str = "static"
    images_dir: str = "static/images"
    
    class Config:
        env_file = ".env"
        
settings = Settings()