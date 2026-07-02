
from pydantic import BaseModel
from datetime import datetime
class Channel(BaseModel):
    id: str
    title: str
    description: str
    published_at: datetime
    subscriber_count: int
    video_count: int
    view_count: int