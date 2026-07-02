# models/comment.py
from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from models.video import Video


class Comment(SQLModel, table=True):
    __tablename__ = 'comments'

    id: Optional[int] = Field(default=None, primary_key=True)
    video_id: str = Field(foreign_key="videos.id")
    text: str
    author: str
    published_at: datetime

    video: Optional["Video"] = Relationship(back_populates="comments")