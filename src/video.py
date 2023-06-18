import os
import json
from googleapiclient.discovery import build
from src.channel import Channel


class Video():
    api_key = os.getenv('YT_API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, video_id):
        self.__video_id = video_id
        self.video = self.youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                               id=video_id
                                               ).execute()
        self.video_title: str = self.video['items'][0]['snippet']['title']
        self.view_count: int = self.video['items'][0]['statistics']['viewCount']
        self.like_count: int = self.video['items'][0]['statistics']['likeCount']
        self.url = f'https://www.youtube.com/watch?v={video_id}'

    def __str__(self):
        return self.video_title

    @property
    def video_id(self):
        return self.__video_id

class PLVideo(Video):
    ...