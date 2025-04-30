import re
import time 
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

class YoutubeStreamHandler:
    def __init__(self, client_secret_path = "venv/Client_Secret.json"):
        self.scopes = ["https://www.googleapis.com/auth/youtube.readonly"]
        self.credentials = None
        self.youtube = None
        self.live_chat_id = None
        self.video_id = None
        self._auth(client_secret_path)

    def _auth(self, client_secret_path):
        flow = InstalledAppFlow.from_client_secrets_file(client_secret_path, self.scopes)
        self.credentials = flow.run_local_server(port=0)
        self.youtube = build("youtube", "v3", credentials= self.credentials)

    def SetStream(self, url):
        match = re.search(r"v=([a-zA-Z0-9_-]{11})")
        if not match:
            raise ValueError("Invalid youtube stream URL")
        self.video_id = match.group(1)

        video_response = self.youtube.videos().list(
            part="liveStreamingDetails",
            id = self.video_id
        ).execute()

        try:
            self.live_chat_id = video_response["items"][0]["liveStreamDetails"]["activeLiveChatId"]
        except (KeyError, IndexError):
            raise RuntimeError("Live chat not in this stream")
        
    def GetChat(self, num_chat = 10):
        if not self.live_chat_id:
            raise RuntimeError("Live not set yet")
        response = self.youtube.liveChatMessages().list(
            liveChatId = self.live_chat_id,
            part = "snippet,authorDetails"
        ).execute()

        message = []
        for item in reversed(response["items"][-num_chat:]):
            msg = {
                "author": item["authorDetails"]["displayName"],
                "message": item["snippet"]["displayMessage"]
            }
            message.append(msg)
        return message
    def GetChainChat(self, num_chat = 10):
        if not self.live_chat_id:
            raise RuntimeError("Not set live chat in this stream yet")
        response = self.youtube.liveChatMessages().list(
            liveChatId = self.live_chat_id,
            part = "snippet"
        ).execute()

        items = response["items"][-num_chat:]
        chain = ""

        for item in reversed(items):
            msg = item["snippet"]["displayMessage"].strip()
            if len(msg) == 1:
                chain += msg
            else:
                chain += " " 
        return chain.strip()
    

        