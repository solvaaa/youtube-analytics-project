import datetime
import os
import isodate
from googleapiclient.discovery import build
import datetime

class PlayList:
    """ Класс для плейлиста """
    api_key = os.getenv('YT_API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, playlist_id):
        self.playlist_id = playlist_id
        self.playlist = self.youtube.playlists().list(id=self.playlist_id, part='snippet').execute()
        self.playlist_videos = self.youtube.playlistItems().list(playlistId=playlist_id,
                                               part='contentDetails,snippet',
                                               maxResults=50,
                                               ).execute()
        video_ids = [video['contentDetails']['videoId'] for video in self.playlist_videos['items']]
        self.video_response = self.youtube.videos().list(part='contentDetails,statistics',
                                               id=','.join(video_ids)
                                               ).execute()
        self.url = 'https://www.youtube.com/playlist?list=' + playlist_id
        self.title = self.playlist['items'][0]['snippet']['title']

    @property
    def total_duration(self):
        total_duration = datetime.timedelta(0)
        for video in self.video_response['items']:
            iso_8601_duration = video['contentDetails']['duration']
            duration = isodate.parse_duration(iso_8601_duration)
            total_duration += duration
        return total_duration

    def show_best_video(self):
        max_likeCount = -1
        max_likeCount_id = 0
        for video in self.video_response['items']:
            current_likes = int(video['statistics']['likeCount'])
            if current_likes > max_likeCount:
                max_likeCount = current_likes
                max_likeCount_id = video['id']
        url_max_likeCount = "https://youtu.be/" + max_likeCount_id
        return url_max_likeCount

