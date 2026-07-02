    

from pydantic import BaseModel
from datetime import datetime
from pydantic import BaseModel

class Comment(BaseModel):
    text: str
    author: str
    published_at: datetime