from fastapi import FastAPI
from app.core.logging import setup_logging
from app.api import api_router
from langgraph.checkpoint.postgres.aio import AsyncPostgresSaver
from contextlib import asynccontextmanager
from psycopg.rows import dict_row
from psycopg_pool import AsyncConnectionPool
from app.core.config import settings
from app.agents.blog_writer.graph import build_graph
from app.db import get_engine, get_session_factory
from app.core.exception_handlers import register_exception_handlers

@asynccontextmanager
async def lifespan(app: FastAPI):
    engine = get_engine()
    try:
        async with AsyncConnectionPool(
                    conninfo=settings.database_url.get_secret_value(),
                    max_size=10,
                    open=False,
                    kwargs={
                        "autocommit": True, 
                        "prepare_threshold": 0,
                        "row_factory": dict_row
                    }
                ) as pool:
                    checkpointer = AsyncPostgresSaver(pool)
                    await checkpointer.setup()
                    app.state.writer = build_graph(checkpointer=checkpointer)
                    app.state.session_factory = get_session_factory(engine)
                    yield 
    finally:
          await engine.dispose()



def create_app() -> FastAPI:
    setup_logging()
    app = FastAPI(
        title="Blog Writer AI",
        description="An AI powered blog writing api for my personal website using fastapi and langgraph.",
        version="1.0.0",
        lifespan=lifespan
    )

    register_exception_handlers(app)

    app.include_router(router=api_router)

    return app

app = create_app()
