
import requests
from Enums.YoutubeApiEnums import DataPieceEnum, DataPieceTypeEnum
from Enums.ResponseEnums import ResponseEnum
from Enums.YoutubeApiEnums import ResponseKeyEnum
import logging

logger = logging.getLogger(__name__)
class APIClient:
    def __init__(self, api_key, base_url, timeout=10):
        self.api_key = api_key
        self.base_url = base_url
        self.timeout = timeout

    def _get(self, endpoint: str, params: dict) -> dict | None:
        """Centralized GET with timeout + error handling. Returns None on failure."""
        url = f'{self.base_url}/{endpoint}'
        response = None
        try:
            response = requests.get(url, params=params, timeout=self.timeout)
        except requests.exceptions.Timeout:
            logger.error(ResponseEnum.TimeoutError.value.format(endpoint=endpoint, params=params))
            return None
        except requests.exceptions.ConnectionError:
            logger.error(ResponseEnum.ConnectionError.value.format(endpoint=endpoint, params=params))
            return None
        except requests.exceptions.RequestException as e:
            logger.error(ResponseEnum.RequestError.value.format(endpoint=endpoint, e=e))
            return None

        if response.status_code != 200:
            logger.error(
                ResponseEnum.NON_200_RESPONSE.value.format(
                    endpoint=endpoint,
                    status=response.status_code,
                    body=response.text[:300]
                )
            )
            return None

        try:
            return response.json()
        except ValueError:
            logger.error(ResponseEnum.INVALID_JSON.value.format(endpoint=endpoint, body=response.text[:300]))
            return None
    
    def get_channel_data(self, handle: str):
        """Fetch channel data and uploads playlist ID for a given handle."""
        params = {
            'part': f'{DataPieceTypeEnum.SNIPPET.value},{DataPieceTypeEnum.STATISTICS.value},{DataPieceTypeEnum.CONTENT_DETAILS.value}',
            'forHandle': handle,
            'key': self.api_key
        }
        data = self._get(DataPieceEnum.CHANNELS.value, params)
        ITEMS = ResponseKeyEnum.ITEMS.value
        if ITEMS not in data or not data[ITEMS]:
            logger.error(ResponseEnum.NO_CHANNEL_FOUND.value.format(handle=handle))
            return None, None
        
        channel = data[ITEMS][0]
        uploads_playlist_id = channel[DataPieceTypeEnum.CONTENT_DETAILS.value][DataPieceTypeEnum.RELATED_PLAYLISTS.value][DataPieceTypeEnum.UPLOADS.value]
        return channel, uploads_playlist_id

    def get_all_video_ids(self, playlist_id: str):
        """Page through the uploads playlist to collect every video ID."""
        video_ids = []
        next_page_token = None

        while True:
            params = {
                'part': DataPieceTypeEnum.CONTENT_DETAILS.value,
                'playlistId': playlist_id,
                'maxResults': 50,
                'key': self.api_key
            }
            if next_page_token:
                PAGE_TOKEN = DataPieceTypeEnum.PAGE_TOKEN.value
                params[PAGE_TOKEN] = next_page_token

            data = self._get(DataPieceEnum.PLAYLIST.value + 'Items', params)
            if data is None:
                logger.warning(ResponseEnum.FAILED_TO_FETCH_PLAYLIST_ITEMS.value.format(playlist_id=playlist_id))
                break

            ITEMS = ResponseKeyEnum.ITEMS.value
            for item in data.get(ITEMS, []):
                video_ids.append(item[DataPieceTypeEnum.CONTENT_DETAILS.value]['videoId'])

            next_page_token = data.get(ResponseKeyEnum.NEXT_PAGE_TOKEN.value)
            if not next_page_token:
                break

        return video_ids
    
    def get_videos_data(self, video_ids: list):
        """Batch-fetch full stats/snippet data for videos (50 per request max)."""
        all_videos = []

        for i in range(0, len(video_ids), 50):
            chunk = video_ids[i:i + 50]
            params = {
                'part': f'{DataPieceTypeEnum.SNIPPET.value},{DataPieceTypeEnum.STATISTICS.value},{DataPieceTypeEnum.CONTENT_DETAILS.value}',
                'id': ','.join(chunk),
                'key': self.api_key
            }
            data = self._get(DataPieceEnum.VIDEOS.value, params)
            ITEMS = ResponseKeyEnum.ITEMS.value
            all_videos.extend(data.get(ITEMS, []))

        return all_videos
    def get_video_comments(self, video_id):
        params = {
            'part': DataPieceTypeEnum.SNIPPET.value,
            'videoId': video_id,
            'key': self.api_key
        }
        data = self._get(DataPieceEnum.COMMENT_THREADS.value, params)
        return data.get(ResponseKeyEnum.ITEMS.value, []) 