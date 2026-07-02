from pydantic import BaseModel
from datetime import datetime
from typing import List
from .comment import Comment


class Video(BaseModel):
    id: str
    title: str
    channel: str
    published_at: datetime
    view_count: int
    like_count: int
    comment_count: int
    comments: List[Comment] = []