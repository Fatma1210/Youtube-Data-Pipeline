from enum import Enum

class ResponseEnum(str, Enum):
    """Enum for different types of responses."""
    NO_CHANNEL_FOUND = "No channel found for handle: {handle}"
    TimeoutError = "Request to {endpoint} timed out with {params}."
    ConnectionError = "Connection error calling {endpoint} with params={params}."
    RequestError = "Request failed for {endpoint}: {e}" 
    NON_200_RESPONSE = "Non-200 response from {endpoint}: status={status}, body={body}"
    INVALID_JSON = "Invalid JSON from {endpoint}: {body}"
    FAILED_TO_FETCH_PLAYLIST_ITEMS = "Failed to fetch playlist items for playlist_id: {playlist_id}"
    FAILED_TO_FETCH_COMMENTS = "Failed to fetch comments for video ID: {video_id}"