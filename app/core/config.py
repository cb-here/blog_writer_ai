from pydantic_settings import SettingsConfigDict, BaseSettings
from pydantic import SecretStr

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=False,
        extra="ignore"
    )

    openai_api_key: SecretStr
    chat_model_name: str
    database_url: SecretStr

    @property
    def sqlalchemy_database_url(self) -> str:
        return self.database_url.get_secret_value().replace(
            "postgresql://",
            "postgresql+psycopg://",
            1,
        )

settings = Settings()