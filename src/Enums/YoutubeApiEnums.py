from enum import Enum

class DataPieceEnum(str, Enum):
    """Enum for different pieces of data."""
    CHANNELS = "channels"
    PLAYLIST = "playlist"
    VIDEOS = "videos"
    COMMENT_THREADS = "commentThreads"

class DataPieceTypeEnum(str, Enum):
    """Enum for different types of data pieces."""
    SNIPPET = "snippet"
    STATISTICS = "statistics"
    CONTENT_DETAILS = "contentDetails"
    RELATED_PLAYLISTS = "relatedPlaylists"
    UPLOADS = "uploads"
    PAGE_TOKEN = "pageToken"
    
class ResponseKeyEnum(str, Enum):
    """Enum for keys used when parsing API response JSON."""
    ITEMS = "items"
    ID = "id"
    NEXT_PAGE_TOKEN = "nextPageToken"
    KIND = "kind"
    ETAG = "etag"
    TOP_LEVEL_COMMENT = "topLevelComment"
    TOTAL_REPLY_COUNT = "totalReplyCount"

class VideoDataPieceEnum(str, Enum):
    """Enum for different pieces of video data."""
    SNIPPET = "snippet"
    TITLE = "title"
    DESCRIPTION = "description"
    PUBLISHED_AT = "publishedAt"
    STATISTICS = "statistics"
    VIEW_COUNT = "viewCount"
    LIKE_COUNT = "likeCount"
    COMMENT_COUNT = "commentCount"

class CommentDataPieceEnum(str, Enum):
    """Enum for different pieces of comment data."""
    SNIPPET = "snippet"
    TEXT_DISPLAY = "textDisplay"
    AUTHOR_DISPLAY_NAME = "authorDisplayName"
    PUBLISHED_AT = "publishedAt"

class ChannelDataPieceEnum(str, Enum):
    """Enum for different pieces of channel data."""
    SNIPPET = "snippet"
    TITLE = "title"
    DESCRIPTION = "description"
    PUBLISHED_AT = "publishedAt"
    STATISTICS = "statistics"
    SUBSCRIBER_COUNT = "subscriberCount"
    VIDEO_COUNT = "videoCount"
    VIEW_COUNT = "viewCount"