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
        self.__channel_id = channel_id
        self.channel = self.youtube.channels().list(id=channel_id, part='snippet,statistics').execute()

    @property
    def channel_id(self):
        return self.__channel_id
    @property
    def title(self):
        return self.channel['items'][0]['snippet']['title']

    @property
    def description(self):
        return self.channel['items'][0]['snippet']['description']

    @property
    def subscriber_count(self):
        return self.channel['items'][0]['statistics']['subscriberCount']

    @property
    def video_count(self):
        return int(self.channel['items'][0]['statistics']['videoCount'])

    @property
    def view_count(self):
        return int(self.channel['items'][0]['statistics']['viewCount'])

    @property
    def url(self):
        url_ = 'https://www.youtube.com/channel/'
        return url_ + self.channel_id



    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print(json.dumps(self.channel, indent=2, ensure_ascii=False))

    def to_json(self, path):
        pass

    @classmethod
    def get_service(cls):
        return cls.youtube
