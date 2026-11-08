from fastapi import APIRouter, Depends, Query
from app.dependencies.writer import get_writer
from app.dependencies.session  import get_session
from app.schemas.blog import BlogRequest, BlogResponse, BlogSummary
from app.services import blog_service
from uuid import UUID

router = APIRouter()

@router.post("/", response_model=BlogResponse)
async def write_blog(request: BlogRequest, writer=Depends(get_writer), session=Depends(get_session)):
    result = await blog_service.write_blog_service(writer=writer, session=session, topic=request.topic)

    return result

@router.get("/{id}", response_model=BlogResponse)
async def get_blog(
    id: UUID, 
    session=Depends(get_session)
):
    return await blog_service.get_blog_service(session, id)

@router.get("/",response_model=list[BlogSummary])
async def get_blogs(
    limit: int = Query(20, ge=1, le=100),
    offset: int = Query(0, ge=0),
    search: str | None = Query(None, max_length=200),
    session = Depends(get_session)
):
    return await blog_service.list_blogs_service(session, limit, offset, search)