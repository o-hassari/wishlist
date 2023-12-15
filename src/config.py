from pydantic import BaseSettings


class Settings(BaseSettings):
    db_hostname: str
    db_port: str
    db_password: str
    db_name: str
    db_username: str

    jwt_secret_key: str
    jwt_refresh_secret_key: str
    algorithm: str
    access_token_expire_minutes: int
    refresh_token_expire_minutes: int

    #model_config = SettingsConfigDict(env_file='.env', extra='ignore')

    class Config:
        env_file = ".env"


#_env_file=None
settings = Settings()