from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
  database_hostname: str
  database_port: int
  database_password: str
  database_name: str
  database_username: str

  # CONFIG (Auto fills the data from .env)
  model_config = SettingsConfigDict(env_file = ".env")

settings = Settings()