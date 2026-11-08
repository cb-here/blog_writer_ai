from app.utils.runnable_config import generate_runnable_config
from uuid import uuid4
from app.repositories import blog_repository
from app.core.exceptions import BlogNotFound
from app.db.models import Blog
from sqlalchemy import RowMapping

async def write_blog_service(writer, session, topic: str) -> Blog:
    thread_id = uuid4()
    config = generate_runnable_config(str(thread_id))

    response = await writer.ainvoke({
        "topic": topic
    }, config=config)

    blog = await blog_repository.create_blog(session, thread_id, topic=response["topic"], title=response["title"], content=response["content"])


    return blog

async def get_blog_service(session, id) -> Blog:
    blog = await blog_repository.get_blog(session, id)

    if blog is None:
        raise BlogNotFound()

    return blog

async def list_blogs_service(
    session, limit: int, offset: int, search: str | None = None
) -> list[RowMapping]:
    return await blog_repository.list_blogs(session, limit, offset, search)
