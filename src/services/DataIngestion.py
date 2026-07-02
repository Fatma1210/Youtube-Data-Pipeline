from mappers.ChannelMapper import ChannelMapper
from mappers.VideoMapper import VideoMapper
from mappers.CommentMapper import CommentMapper


class DataIngestion:
    def __init__(self, api_client):
        self.api_client = api_client

    def ingest_data(self, handle):
        raw_channel, uploads_playlist_id = self.api_client.get_channel_data(handle)
        if raw_channel is None:
            return None, [], {}

        channel = ChannelMapper.to_model(raw_channel)

        video_ids = self.api_client.get_all_video_ids(uploads_playlist_id)
        raw_videos = self.api_client.get_videos_data(video_ids)

        videos = []
        comments_by_video = {}

        for raw_video in raw_videos:
            video = VideoMapper.to_model(raw_video, channel.id)
            videos.append(video)

            raw_comments = self.api_client.get_video_comments(video.id)
            comments_by_video[video.id] = CommentMapper.to_model_list(raw_comments, video.id)

        return channel, videos, comments_by_video