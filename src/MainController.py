from src.ServerHandle import server_commands
from src.StreamHandle.Stream_Handler import YoutubeStreamHandler

import time
import threading
import keyboard

class MainControll:
    def __init__(self, stream_url: str, target_player: str, _DelayTime = 1):
        self.running = True
        self.pause = True
        self.target_player = target_player
        self.stream_url = stream_url
        self.yt_handler = YoutubeStreamHandler()
        self.yt_handler.set_stream(self.stream_url)
        self.yt_handler.meaning_word = [
            "ZOMB", "FLING", "EXPLO", "CREEP", "BLIND", 
            "FISH", "FALL", "FLY", "SFI", "DUNGEON", 
            "BOX", "WET", "KRO"
        ]
        self.delay_time = _DelayTime

    def MainRun(self):
        chain = self.yt_handler.GetChainChat(NumChat)
        word = self.yt_handler.GetNextWord()
        print("Current chain :",chain)
        self.yt_handler.SaveCurrentTime()
        TargetPlayer = self.target_player
        while word and self.running:

                match word:
                    case "WET":
                        print("Spawn water")
                        server_commands.summon_Water(TargetPlayer, 20)
                    case "SFI":
                        server_commands.summon_SilverFish(TargetPlayer)
                    case "ZOMB":
                        print("spawn zombie")
                        server_commands.summon_SpecialZombie(TargetPlayer)
                        server_commands.give_effect(TargetPlayer, "slowness", 20, 3)
                    case "CREEP":
                        print("Spawn screeper")
                        server_commands.summon_SpecialCreeper(TargetPlayer,30,20)
                    case "FLING":
                        print("fling player")
                        server_commands.FlyTroll(TargetPlayer)
                        
                    case "EXPLO":
                        print("TNT player")
                        server_commands.summon_TNT(TargetPlayer)
                    case "BLIND":
                        print("Blind player")
                        server_commands.give_effect(TargetPlayer, "darkness", 180, 2)
                    case "FLY":
                        print("Fly player")
                        server_commands.give_effect(TargetPlayer, "levitation", 7, 1)
                        for i in range(20):
                            server_commands.summon(TargetPlayer, "skeleton")
                            time.sleep(0.1)
                    case "FALL":
                        print("Fall troll player")
                        server_commands.FallTroll(TargetPlayer, 25)
                    
                    case "FISH":
                        print("Spawn fish")
                        server_commands.summon_Guardian(TargetPlayer)
                        server_commands.summon_Guardian(TargetPlayer)
                        server_commands.summon_Guardian(TargetPlayer)
             
                    case "DUNGEON":
                        print("Spawn Dungoen")
                        server_commands.summon_Box(TargetPlayer, 6)
                        server_commands.give_effect(TargetPlayer, "weakness", 20, 3)
                        server_commands.give_effect(TargetPlayer, "slowness", 20, 2)
                        for i in range(20):
                            server_commands.summon_zombie_at(TargetPlayer)
                            time.sleep(0.1)
                        for i in range(10):
                            server_commands.summon_creeper(TargetPlayer)
                            time.sleep(0.1)
                        for i in range(30):
                            server_commands.summon_SilverFish(TargetPlayer)
                            time.sleep(0.1)
                    case "BOX":
                        server_commands.summon_Box(TargetPlayer, 5)
                    case "KRO":
                        server_commands.summon_GiantZombie(TargetPlayer)
                    case _:
                        print("Nothing found")

                
            time.sleep(self.delay_time)