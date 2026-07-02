from sqlmodel import Session
from models.channel import Channel
from models.video import Video
from models.comment import Comment


class YoutubeRepository:
    def __init__(self, db):
        self.db = db

    def save(self, channel: Channel, videos: list[Video], comments_by_video: dict[str, list[Comment]]):
        """Persist a channel, its videos, and their comments in one transaction."""
        with self.db.get_session() as session:
            session.merge(channel)

            for video in videos:
                session.merge(video)
                for comment in comments_by_video.get(video.id, []):
                    session.add(comment)

            session.commit()