# models/video.py
from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime
from typing import List, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from models.channel import Channel
    from models.comment import Comment


class Video(SQLModel, table=True):
    __tablename__ = 'videos'

    id: str = Field(primary_key=True)
    title: str
    channel_id: str = Field(foreign_key="channels.id")
    published_at: datetime
    view_count: int = 0
    like_count: int = 0
    comment_count: int = 0

    channel: Optional["Channel"] = Relationship(back_populates="videos")
    comments: List["Comment"] = Relationship(back_populates="video")