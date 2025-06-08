from src.ServerHandle import server_commands
from src.StreamHandle.Stream_Handler import YoutubeStreamHandler
from src.MainController import MainControll
import time
import threading
import keyboard

DelayTime = 10
NumChat = -1
running = True
Pause = True
TargetPlayer = "Tuna_TheFish"
Stream_URL = "https://youtu.be/4CszJGNnYz4"

mainControll1 = MainControll(Stream_URL, TargetPlayer, DelayTime)


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
            mainControll1.MainRun()
        else :
            time.sleep(1)
    
    print("Stop program")
