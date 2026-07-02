import re
from typing import List
import html
import emoji
from models.video import Video as VideoModel
from models.comment import Comment as CommentModel
from datetime import datetime


class DataTransformation:
    """Class for data transformation methods."""

    @staticmethod
    def strip_emojis(text: str) -> str:
        """Remove emoji characters, keep everything else (punctuation, numbers, etc.)."""
        return emoji.replace_emoji(text, replace='')
    @staticmethod
    def strip_html(text: str) -> str:
        """Remove HTML tags and decode HTML entities (e.g. &amp; -> &, &#39; -> ')."""
        text = html.unescape(text)                    
        text = re.sub(r'<[^>]+>', '', text)            
        return text
  
    @staticmethod
    def is_low_quality_comment(text: str, min_length: int = 3) -> bool:
        """A comment is low-quality/noise if, after cleaning, it's empty or too short to carry meaning."""
        cleaned = DataTransformation.normalize_text(text)
        return len(cleaned) < min_length
    @staticmethod
    def normalize_text(text: str) -> str:
        """Strip HTML, strip emojis, normalize whitespace, and trim text."""
        text = DataTransformation.strip_html(text)
        text = DataTransformation.strip_emojis(text)
        text = DataTransformation.normalize_whitespace(text)
        return text.strip()
    @staticmethod
    def normalize_whitespace(text: str) -> str:
        """Collapse multiple spaces/newlines into single spaces, trim ends."""
        return re.sub(r'\s+', ' ', text).strip()

    @staticmethod
    def parse_youtube_datetime(value: str) -> datetime:
        """Convert YouTube API's ISO 8601 string ('...Z' suffix) into a datetime object."""
        return datetime.fromisoformat(value.replace('Z', '+00:00'))

    @staticmethod
    def transform_videos(videos: List[VideoModel]) -> List[VideoModel]:
        """Clean video fields in place (normalize title text)."""
        for video in videos:
            video.title = DataTransformation.normalize_text(video.title)
        return videos

    @staticmethod
    def transform_comments(comments_by_video: dict[str, List[CommentModel]]) -> dict[str, List[CommentModel]]:
        """Clean comment fields and drop low-quality (empty/too-short) comments."""
        for video_id, comments in comments_by_video.items():
            cleaned_comments = []
            for comment in comments:
                comment.author = DataTransformation.normalize_text(comment.author)
                comment.text = DataTransformation.normalize_text(comment.text)

                if not DataTransformation.is_low_quality_comment(comment.text):
                    cleaned_comments.append(comment)

            comments_by_video[video_id] = cleaned_comments
        return comments_by_video