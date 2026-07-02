
from Enums.YoutubeApiEnums import DataPieceTypeEnum , ResponseKeyEnum
from mappers import ChannelMapper
from mappers import VideoMapper
from mappers import CommentMapper



class DataIngestion:
    def __init__(self, api_client):
        self.api_client = api_client

    def ingest_data(self, handle):
        channel, uploads_playlist_id = self.api_client.get_channel_data(handle)
        channel_model = ChannelMapper.to_model(channel)
        print("Channel:", channel_model.title)
        print("Subscribers:", channel_model.subscriber_count)
        print("Total videos (reported):", channel_model.video_count)

        video_ids = self.api_client.get_all_video_ids(uploads_playlist_id)
        print(f"Found {len(video_ids)} videos")

        videos = self.api_client.get_videos_data(video_ids)
        video_models = [VideoMapper.to_model(video, channel_model.title, []) for video in videos]
        for video in video_models[:5]:
            print(video.title)
            print(video.published_at, 'published on')
            print(video.view_count, 'views')
            print(video.like_count, 'likes')
            print(video.comment_count, 'comments')

           
            comments = self.api_client.get_video_comments(video.id)
            comment_models = CommentMapper.to_model_list(comments)
            for comment in comment_models[:3]:
                print("Comment:",comment.text)
                print("By:",comment.author)
                print("Published at:",comment.published_at)
        return videos