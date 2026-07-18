from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import PostgresDsn
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

class DbSettings(BaseSettings):
    port: int
    password: str
    user: str
    name: str
    host: str
    dialect: str

    @property
    def get_async_db_url(self):
        return PostgresDsn.build(
            scheme=self.dialect,
            username=self.user,
            password=self.password,
            host=self.host,
            port=self.port,
            path=self.name
        )
    
    @property
    def get_sync_db_url(self):
        return PostgresDsn.build(
            scheme="postgresql",
            username=self.user,
            password=self.password,
            host=self.host,
            port=self.port,
            path=self.name  
        )
    
    

    

class Settings(BaseSettings):
    DB: DbSettings

    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".env",
        env_nested_delimiter="_"
    )


settings = Settings()



