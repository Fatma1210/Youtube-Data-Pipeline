import os
import requests
from services.DataTransformation import DataTransformation
from dotenv import load_dotenv
from clients.APIClient import APIClient
from services.DataIngestion import DataIngestion
from config import Settings
from database.db import Database
from database.repository import YoutubeRepository
from services.DataStorage import DataStorage

db = Database('youtube_data.db')

settings = Settings()
BASE_URL = settings.BASE_URL
api_key = settings.API_KEY
handles = settings.HANDLES
client = APIClient(api_key, BASE_URL)

data_ingestion = DataIngestion(client)

if __name__ == '__main__':
    db.create_tables()
    repository = YoutubeRepository(db)
    for handle in handles:
        print(f"\nIngesting data for channel handle: {handle}")
        try:
            channel, videos, comments_by_video = data_ingestion.ingest_data(handle)
            if channel is None:
                print(f"Skipping {handle} — could not fetch channel data")
                continue

            videos = DataTransformation.transform_videos(videos)
            comments_by_video = DataTransformation.transform_comments(comments_by_video)

            DataStorage.store_data(repository, channel, videos, comments_by_video)
            total_comments = sum(len(c) for c in comments_by_video.values())
            print(f"Saved {len(videos)} videos and {total_comments} comments for {handle}")

        except Exception as e:
            print(f"FAILED to process {handle}: {e}")
            import traceback
            traceback.print_exc()
            continue  # don't let one channel's failure kill the whole run
