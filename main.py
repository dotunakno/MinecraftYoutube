from src.ServerHandle import server_commands
from src.StreamHandle.Stream_Handler import YoutubeStreamHandler
if __name__ == "__main__":
    Stream_URL = "https://www.youtube.com/live/wOgQnIDgT2c?si=1Xyr-lDqQ-S2zpJE"
    yt = YoutubeStreamHandler()
    yt.SetStream(Stream_URL)

    chain = yt.GetChainChat(5)
    print("Chat Combine :", chain)
    
