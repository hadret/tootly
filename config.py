from functools import lru_cache
from pydantic import BaseSettings


class Settings(BaseSettings):
    env_name: str = "Local"
    feed_url: str = "http://some.feed/url.xml"
    db_url: str = "sqlite:///./tweetly.db"

    class Config:
        env_file = ".env"


@lru_cache
def get_settings() -> Settings:
    settings = Settings()
    print(f"Loading settings for: {settings.env_name}")
    return settings
