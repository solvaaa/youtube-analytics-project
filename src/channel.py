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
        self.__title = self.channel['items'][0]['snippet']['title']
        self.__description = self.channel['items'][0]['snippet']['description']
        self.__subscriber_count = self.channel['items'][0]['statistics']['subscriberCount']
        self.__video_count = int(self.channel['items'][0]['statistics']['videoCount'])
        self.__view_count = int(self.channel['items'][0]['statistics']['viewCount'])
        self.__url = 'https://www.youtube.com/channel/' + self.channel_id


    @property
    def channel_id(self):
        return self.__channel_id
    @property
    def title(self):
        return self.__title

    @property
    def description(self):
        return self.__description

    @property
    def subscriber_count(self):
        return self.__subscriber_count

    @property
    def video_count(self):
        return self.__video_count

    @property
    def view_count(self):
        return self.__view_count

    @property
    def url(self):
        return self.__url



    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print(json.dumps(self.channel, indent=2, ensure_ascii=False))

    def to_json(self, path):
        attributes = {
            'channel_id': self.channel_id,
            'title': self.title,
            'description': self.description,
            'subscriber_count': self.subscriber_count,
            'video_count': self.video_count,
            'view_count': self.view_count,
            'url': self.url
        }
        output_string = json.dumps(attributes)
        with open(path, 'w', encoding='utf-8') as json_file:
            json_file.write(output_string)

    @classmethod
    def get_service(cls):
        return cls.youtube
