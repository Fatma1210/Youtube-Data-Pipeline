# mappers/video_mapper.py
from models.video import Video
from .CommentMapper import CommentMapper
from Enums.YoutubeApiEnums import DataPieceTypeEnum as data , ResponseKeyEnum as response , VideoDataPieceEnum as video, CommentDataPieceEnum as comment
from services.DataTransformation import DataTransformation
class VideoMapper:
    @staticmethod
    def to_model(raw_video: dict, channel_id: str) -> Video:
        snippet = raw_video[data.SNIPPET.value]
        stats = raw_video[data.STATISTICS.value]

        return Video(
            id=raw_video[response.ID.value],
            title=snippet[video.TITLE.value], 
            channel_id=channel_id,
            published_at=DataTransformation.parse_youtube_datetime(snippet[video.PUBLISHED_AT.value]),
            view_count=int(stats.get(video.VIEW_COUNT.value, 0)),
            like_count=int(stats.get(video.LIKE_COUNT.value, 0)),
            comment_count=int(stats.get(video.COMMENT_COUNT.value, 0)),
        )