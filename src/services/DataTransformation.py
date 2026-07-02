import re
from typing import List
import emoji  # pip install emoji
from models.video import Video as VideoModel


class DataTransformation:
    """Class for data transformation methods."""


    @staticmethod
    def strip_emojis(text: str) -> str:
        """Remove emoji characters, keep everything else (punctuation, numbers, etc.)."""
        return emoji.replace_emoji(text, replace='')

    @staticmethod
    def normalize_text(text: str) -> str:
        """Strip emojis, normalize whitespace, and trim text."""
        text = DataTransformation.strip_emojis(text)
        text = DataTransformation.normalize_whitespace(text)
        return text.strip()
    
    @staticmethod
    def normalize_whitespace(text: str) -> str:
        """Collapse multiple spaces/newlines into single spaces, trim ends."""
        return re.sub(r'\s+', ' ', text).strip()
    def transform_data(self ,videos:List[VideoModel]):
        """Transform a list of VideoModel instances into a structured format."""
        transformed_videos = []
        for video in videos:
            transformed_video = {
                "id": video.id,
                "title": self.normalize_text(video.title),
                "channel": self.normalize_text(video.channel),
                "published_at": video.published_at.isoformat(),
                "view_count": video.view_count,
                "like_count": video.like_count,
                "comment_count": video.comment_count,
                "comments": [
                    {
                        "author": self.normalize_text(comment.author),
                        "text": self.normalize_text(comment.text),
                        "published_at": comment.published_at.isoformat()
                    }
                    for comment in video.comments
                ]
            }
            transformed_videos.append(transformed_video)
        return transformed_videos
        
  