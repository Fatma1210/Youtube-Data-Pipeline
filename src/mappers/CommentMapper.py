# mappers/comment_mapper.py
from tomlkit import comment

from services.DataTransformation  import DataTransformation
from models.comment import Comment
from Enums.YoutubeApiEnums import DataPieceTypeEnum  , VideoDataPieceEnum , CommentDataPieceEnum



class CommentMapper:
    @staticmethod
    def to_model(raw_comment: dict , video_id: str) -> Comment:
        snippet = raw_comment[DataPieceTypeEnum.SNIPPET.value]['topLevelComment'][CommentDataPieceEnum.SNIPPET.value]
        return Comment(
            video_id=video_id,
            text=snippet[CommentDataPieceEnum.TEXT_DISPLAY.value],
            author=snippet[CommentDataPieceEnum.AUTHOR_DISPLAY_NAME.value],
            published_at=DataTransformation.parse_youtube_datetime(snippet[CommentDataPieceEnum.PUBLISHED_AT.value])
        )

    @staticmethod
    def to_model_list(raw_comments: list, video_id: str) -> list[Comment]:
        return [CommentMapper.to_model(c, video_id) for c in raw_comments]