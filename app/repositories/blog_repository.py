from app.db.models import Blog
from sqlalchemy.ext.asyncio import AsyncSession
from uuid import UUID 
from sqlalchemy import select, RowMapping

async def create_blog(session: AsyncSession, thread_id: UUID, topic: str, title: str, content: str) -> Blog:
    blog = Blog(thread_id=thread_id, topic = topic, title = title, content = content)
    session.add(blog)

    await session.commit()

    return blog

async def get_blog(session: AsyncSession, id: UUID) -> Blog |  None:
    return await session.get(Blog, id)

async def list_blogs(session: AsyncSession, limit: int, offset: int, search: str | None = None) -> list[RowMapping]:
    stmt = select(
        Blog.id, 
        Blog.topic,
        Blog.title, 
        Blog.created_at,
        Blog.updated_at
    )

    if search:
        stmt = stmt.where(
            Blog.title.icontains(search, autoescape=True)
        )

    stmt = (
        stmt
        .order_by(Blog.updated_at.desc(), Blog.id)
        .limit(limit)
        .offset(offset)
    )

    result = await session.execute(stmt)

    return list(result.mappings().all())
    
