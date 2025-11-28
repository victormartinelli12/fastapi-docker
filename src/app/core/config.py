from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()


class Config(BaseSettings):
    app_name: str = "Seeds"
    debug: bool = True
    db_user: str = ""
    db_password: str = ""
    db_host: str = ""
    db_name: str = "fastapi_seed"

    @property
    def db_url(self) -> str:
        return f"postgresql://{self.db_user}:{self.db_password}@{self.db_host}:5432/{self.db_name}"


config: Config = Config()