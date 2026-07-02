# mappers/channel_mapper.py
from models.channel import Channel
from Enums.YoutubeApiEnums import ChannelDataPieceEnum, DataPieceTypeEnum as data , ResponseKeyEnum as response , VideoDataPieceEnum as video, CommentDataPieceEnum as comment
from services.DataTransformation  import DataTransformation


class ChannelMapper:
    @staticmethod
    def to_model(raw_channel: dict) -> Channel:
        snippet = raw_channel[data.SNIPPET.value]
        stats = raw_channel[data.STATISTICS.value]

        return Channel(
            id=raw_channel[response.ID.value],
            title=snippet[ChannelDataPieceEnum.TITLE.value],
            description=snippet[ChannelDataPieceEnum.DESCRIPTION.value],
            published_at=DataTransformation.parse_youtube_datetime(snippet[ChannelDataPieceEnum.PUBLISHED_AT.value]),
            subscriber_count=int(stats.get(ChannelDataPieceEnum.SUBSCRIBER_COUNT.value, 0)),
            video_count=int(stats.get(ChannelDataPieceEnum.VIDEO_COUNT.value, 0)),
            view_count=int(stats.get(ChannelDataPieceEnum.VIEW_COUNT.value, 0))
        )   
