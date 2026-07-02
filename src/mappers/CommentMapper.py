# mappers/comment_mapper.py
from tomlkit import comment

from models.comment import Comment
from Enums.YoutubeApiEnums import DataPieceTypeEnum  , VideoDataPieceEnum , CommentDataPieceEnum



class CommentMapper:
    @staticmethod
    def to_model(raw_comment: dict) -> Comment:
        snippet = raw_comment[DataPieceTypeEnum.SNIPPET.value]['topLevelComment'][CommentDataPieceEnum.SNIPPET.value]
        return Comment(
            text=snippet[CommentDataPieceEnum.TEXT_DISPLAY.value],
            author=snippet[CommentDataPieceEnum.AUTHOR_DISPLAY_NAME.value],
            published_at=snippet[CommentDataPieceEnum.PUBLISHED_AT.value]
        )

    @staticmethod
    def to_model_list(raw_comments: list) -> list[Comment]:
        return [CommentMapper.to_model(c) for c in raw_comments]