from pydantic import BaseModel, Field, ConfigDict
from uuid import UUID
from datetime import datetime

class Blog(BaseModel):
    title: str = Field(description="The blog title", max_length=200)
    content: str = Field(description="The complete blog article")

class BlogRequest(BaseModel):
    topic: str = Field(description="The blog topic", min_length=1, max_length=200)

class BlogResponse(BaseModel):
    id: UUID
    thread_id: UUID
    topic: str
    title: str
    content: str 
    created_at: datetime 
    updated_at: datetime | None

class BlogSummary(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    topic: str
    title: str
    created_at: datetime 
    updated_at: datetime | None