import re
import time 
import os
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from dateutil import parser

class YoutubeStreamHandler:
    def __init__(self, client_secret_path = "venv/Client_Secret.json"):
        self.scopes = ["https://www.googleapis.com/auth/youtube.readonly"]
        self.credentials = None
        self.youtube = None
        self.live_chat_id = None
        self.video_id = None
        self.CurrentTime = None
        self.MeaningWord = ["ZOMB", "TNT"]
        self.last_chain = ""
        self.char_time = []
        self.SaveTimeFile = "LastCurrentTime.txt"
        if os.path.exists(self.SaveTimeFile):
            with open(self.SaveTimeFile, "r") as f:
                time_str = f.read().strip()
                self.CurrentTime = parser.isoparse(time_str)
        else :
            self.CurrentTime = None
        self._auth(client_secret_path)

    def _auth(self, client_secret_path):
        flow = InstalledAppFlow.from_client_secrets_file(client_secret_path, self.scopes)
        self.credentials = flow.run_local_server(port=0)
        self.youtube = build("youtube", "v3", credentials= self.credentials)

    def SetStream(self, url):
        match = re.search(r"v=([a-zA-Z0-9_-]{11})", url)
        if not match:
            match = re.search(r"youtu\.be/([a-zA-Z0-9_-]{11})", url)

        if not match:
            raise ValueError("Invalid YouTube stream URL")

        self.video_id = match.group(1)

        video_response = self.youtube.videos().list(
            part="liveStreamingDetails",
            id = self.video_id
        ).execute()

        try:
            self.live_chat_id = video_response["items"][0]["liveStreamingDetails"]["activeLiveChatId"]
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
        items = []
        if num_chat == -1 :
            items = response["items"]
        else: 
            items = response["items"][-num_chat:]
        
        chain = ""
        charTime = []
        for item in items:
            ChatTimeStr = item["snippet"]["publishedAt"]
            ChatTime = parser.isoparse(ChatTimeStr)
            if self.CurrentTime is None or ChatTime > self.CurrentTime:
                msg = item["snippet"]["displayMessage"].strip()

                if len(msg) == 1:
                    chain += msg
                else :
                    chain += " "
                charTime.append(ChatTime)
        
        self.last_chain = chain
        self.char_time = charTime
        return chain.strip()
    
    def GetNextWord(self):
        SmallestIdx = len(self.last_chain) + 1
        GetWord = None
        GetTime = None

        for word in self.MeaningWord:
            
            idx = self.last_chain.find(word)
         
            if idx != -1 and idx < SmallestIdx:
                SmallestIdx = idx
                GetWord = word
                GetTime = self.char_time[idx]
        
        if GetWord:
            self.CurrentTime = GetTime
            return GetWord
        return None

    def SaveCurrentTime(self):
        if self.CurrentTime:
            with open(self.SaveTimeFile, "w") as f:
                f.write(self.CurrentTime.isoformat())

    def ResetTime(self):
        self.CurrentTime = None
        if os.path.exists(self.SaveTimeFile):
            os.remove(self.SaveTimeFile)
        
    

        