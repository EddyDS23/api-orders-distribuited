
from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):

    CORS_ORIGINS:list[str] = ["localhost:3000","localhost:5173"]
    APP_NAME:str = "Api Ordenes Distribuidas"
    APP_DESCRIPTION:str = "Backend con arquitectura clean y enfoque profesional"
    APP_VERSION:str = "1.0.0"
    URL_DATABASE:str

    model_config = {
                    "env_file":".env",
                    "env_file_encoding":"utf-8"
                   }
    
    
@lru_cache
def get_settings() -> Settings:
    return Settings()


