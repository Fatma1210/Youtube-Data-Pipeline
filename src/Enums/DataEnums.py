from enum import Enum

class videoData(str, Enum):
    """Enum for different pieces of data."""
 

class CommentData(str, Enum):
    """Enum for different pieces of data."""
    SNIPPET = "snippet"
    TEXT_DISPLAY = "textDisplay"
    AUTHOR_DISPLAY_NAME = "authorDisplayName"
    PUBLISHED_AT = "publishedAt"