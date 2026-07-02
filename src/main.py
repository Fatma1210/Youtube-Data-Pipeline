import os
import requests
from dotenv import load_dotenv
from clients.APIClient import APIClient
from Enums.YoutubeApiEnums import DataPieceEnum, DataPieceTypeEnum
from services.DataIngestion import DataIngestion
from services.DataTransformation import DataTransformation
from config import Settings
settings = Settings()
BASE_URL = settings.BASE_URL
api_key = settings.API_KEY
handles = settings.HANDLES
client = APIClient(api_key, BASE_URL)

data_ingestion = DataIngestion(client)
data_transformation = DataTransformation()



if __name__ == '__main__':
    for handle in handles:
        print(f"\nIngesting data for channel handle: {handle}")
        videos = data_ingestion.ingest_data(handle)
        transformed_videos = data_transformation.transform_data(videos)
        print(f"Transformed data for {handle}:")
        for video in transformed_videos:
            print(video)
        print(f"Total videos ingested for {handle}: {len(videos)}")