from pydantic import Field
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    jwt_secret_key: str = Field(env="JWT_SECRET_KEY")
    jwt_algo: str = Field(env="JWT_ALGO")
    db_host: str = Field(env="DB_HOST")
    db_port: str = Field(env="DB_PORT")
    db_name: str = Field(env="DB_NAME")
    db_user: str = Field(env="DB_USER")
    db_password: str = Field(env="DB_PASSWORD")

    class Config:
        env_file = ".env"

settings = Settings()
