# models/channel.py
from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from models.video import Video


class Channel(SQLModel, table=True):
    __tablename__ = 'channels'

    id: str = Field(primary_key=True)
    title: str
    description: str = ""
    published_at: datetime
    subscriber_count: int = 0
    video_count: int = 0
    view_count: int = 0

    videos: List["Video"] = Relationship(back_populates="channel")