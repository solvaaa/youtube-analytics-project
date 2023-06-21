import os
import json
from googleapiclient.discovery import build
from pprint import pprint

class PlayList:
    """ Класс для плейлиста """
    api_key = os.getenv('YT_API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, playlist_id):
        self.playlist_id = playlist_id
        self.playlist_videos = self.youtube.playlistItems().list(playlistId=playlist_id,
                                               part='contentDetails,snippet',
                                               maxResults=50,
                                               ).execute()
        self.url = 'https://www.youtube.com/playlist?list=' + playlist_id
        self.title = self.playlist_videos['items'][0]['snippet']['title'].split('.')[0]
