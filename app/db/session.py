from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from app.core.config import settings

def get_engine():
    return create_async_engine(settings.sqlalchemy_database_url, pool_size=5)

def get_session_factory(engine):
    return async_sessionmaker(engine, expire_on_commit=False)