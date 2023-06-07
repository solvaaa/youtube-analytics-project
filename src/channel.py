import os
import json
from googleapiclient.discovery import build
from pprint import pprint


class Channel:
    """Класс для ютуб-канала"""
    api_key = os.getenv('YT_API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id
        self.channel = self.youtube.channels().list(id=channel_id, part='snippet,statistics').execute()
        self.title = self.channel['items'][0]['snippet']['title']
        self.description = self.channel['items'][0]['snippet']['description']
        self.subscriber_count = self.channel['items'][0]['statistics']['subscriberCount']
        self.video_count = int(self.channel['items'][0]['statistics']['videoCount'])
        self.view_count = int(self.channel['items'][0]['statistics']['viewCount'])
        self.url = 'https://www.youtube.com/channel/'
        self.url += channel_id

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print(json.dumps(self.channel, indent=2, ensure_ascii=False))

    def to_json(self, path):
        pass

    @classmethod
    def get_service(cls):
        return cls.youtube
