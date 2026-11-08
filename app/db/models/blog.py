from app.db.base import Base
from sqlalchemy import String, DateTime, func
from sqlalchemy.orm import mapped_column, Mapped
from uuid import UUID, uuid4
from datetime import datetime

class Blog(Base):
    __tablename__ = "blogs"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4)
    thread_id: Mapped[UUID] = mapped_column(index=True)
    topic: Mapped[str] = mapped_column(String(200))
    title: Mapped[str] = mapped_column(String(200))
    content: Mapped[str] = mapped_column(String())
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), index=True)

