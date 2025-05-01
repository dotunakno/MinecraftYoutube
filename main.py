from src.ServerHandle import server_commands
from src.StreamHandle.Stream_Handler import YoutubeStreamHandler

import time
import threading
import keyboard

DelayTime = 10
NumChat = -1
running = True
Pause = True
TargetPlayer = "Tuna_TheFish"
Stream_URL = "https://youtu.be/4CszJGNnYz4"


actions = {
    "ZOMB": lambda: print("Zombie chain")
}


def ExitEvent():
    global running
    keyboard.wait('g')
    print("Key G pressed. Thanks for using Tuna program")
    running = False

def PauseEvent():
    global Pause
    global running
    while(running):
        keyboard.wait('h')
        if Pause == True:
            Pause = False
        else:
            Pause = True
        print(f"Key h pressed, change pause state to {Pause}")

def ResetTimeEvent():
    global yt
    while(running):
        keyboard.wait('j')
        yt.ResetTime()
        print("key j pressed, reset time chat to 0")


yt = YoutubeStreamHandler()
yt.SetStream(Stream_URL)
yt.MeaningWord = ["ZOMB", "FLING", "EXPLO", "CREEP", "BLIND", "FISH", "FALL", "FLY", "SFI", "DUNGEON", "BOX", "WET", "KRO"]       

if __name__ == "__main__":
   
    InputThread = threading.Thread(target=ExitEvent)
    InputThread.daemon = True
    InputThread.start()

    PauseInputStread = threading.Thread(target=PauseEvent)
    PauseInputStread.daemon = True
    PauseInputStread.start()

    ResetTimeThread = threading.Thread(target=ResetTimeEvent)
    ResetTimeThread.daemon = True
    ResetTimeThread.start()


    while(running):
        if(Pause == False):
            chain = yt.GetChainChat(NumChat)
            word = yt.GetNextWord()
            print("Current chain :",chain)
            yt.SaveCurrentTime()
    
            while word and running:

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
                yt.GetChainChat(NumChat)
                word = yt.GetNextWord()

                time.sleep(1)
                
            time.sleep(DelayTime)
        else :
            time.sleep(1)
    
    print("Stop program")
