
from pytube import YouTube
import os
import webbrowser
import pyautogui
import shutil
import colorama
import random
import time
import keyboard
import json
from colorama import Fore, Back, Style
colorama.init(autoreset=True)


# os.system('mode con: cols=80 lines=30')

# ========================================

RED = F"{Fore.RED}"
GREEN = F"{Fore.GREEN}"
YELLOW = F"{Fore.YELLOW}"
BLUE = F"{Fore.BLUE}"
MAGENTA = F"{Fore.MAGENTA}"
CYAN = F"{Fore.CYAN}"
WHITE = F"{Fore.WHITE}"

LRED = F"{Fore.LIGHTRED_EX}"
LGREEN = F"{Fore.LIGHTGREEN_EX}"
LYELLOW = F"{Fore.LIGHTYELLOW_EX}"
LBLUE = F"{Fore.LIGHTBLUE_EX}"
LMAGENTA = F"{Fore.LIGHTMAGENTA_EX}"
LCYAN = F"{Fore.LIGHTCYAN_EX}"
LWHITE = F"{Fore.LIGHTWHITE_EX}"


pauseKey = "ctrl"
resumeKey = "ctrl"
timeoutForEachVideo = 15
initialTimeOut = 8
waitBeforeRefresh = 15
global totalVideoCount
totalVideoCount = 0

file = "./tillNow.txt"
global total
total = 0
store = []


def addition(total):
    with open(file, "a") as f:
        f.write(f"\n{str(total)}")


def initialRead():
    with open(file, "r") as f:
        lines = f.readlines()
        for line in lines:
            s = line.rsplit(" ")
            store.append(s[0])


def getVideoUrl():
    url = driver.current_url
    video = f"{url}"
    yt = YouTube(video)  # this creates a YOUTUBE OBJECT
    video_length = yt.length
    return video_length


def init():
    """Initializes the program"""
    os.system("cls")

    initialRead()
    print(f"{LYELLOW}Initiating script !!!", end="\n")
    print(f"Switch your cursor to Youtube window", end="\n")

    for i in range(initialTimeOut+1, 0, -1):
        time.sleep(1)
        print(f"\r{LYELLOW}Starting in {i} seconds", end="")

    print(f"", end="\n")
    os.system("cls")

    total = store[-1]
    # print(f"{store}",end="\n")
    # print(f"{total}",end="\n")
    print(f"{LGREEN}Total videos watched till now {total}", end="\n")
    print(f"{LGREEN}Total videos watched {totalVideoCount}", end="\n")
    main(totalVideoCount, total)


def main(totalVideoCount, total):
    #c = getVideoUrl()
    c = timeoutForEachVideo
    while c > 0:
        print(f"\r{LCYAN}{c} second(s)\t{LGREEN}{'▆'*c:10} ", end="")
        #for k in range(c): print(f"\r{'▆'*c}", end="")
        #if keyboard.read_key() == pauseKey: print("Paused")
        time.sleep(1)
        c -= 1
    totalVideoCount += 1
    total = int(total)+1
    addition(total)
    os.system("cls")
    initialRead()
    print(f"{LGREEN}Total videos watched till now {total}", end="\n")
    print(f"{LGREEN}Total videos watched {totalVideoCount}", end="\n")
    pyautogui.press("down")
    time.sleep(1)
    main(totalVideoCount, total)


if __name__ == "__main__":
    init()
    # main(totalVideoCount,total)
