import pyperclip
from pytube import YouTube
import os
import pyautogui
import colorama
import time
from colorama import Fore, Back, Style
from youtubeVideoLength import get_video_length

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
initialTimeOut = 9
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

    for i in range(initialTimeOut + 1, 0, -1):
        time.sleep(1)
        print(f"\r{LYELLOW}Starting in {i} seconds", end="")

    print(f"", end="\n")
    os.system("cls")

    try:
        total = store[-1]
    except Exception as e:
        total = 0

    # print(f"{store}",end="\n")
    # print(f"{total}",end="\n")
    print(f"{LGREEN}Total videos watched till now {total}", end="\n")
    print(f"{LGREEN}Total videos watched {totalVideoCount}", end="\n")
    main(totalVideoCount, total)

def getVideoId(url):
    videoId = url.split("/shorts/")[1]
    return videoId

def main(totalVideoCount, total):
    pyautogui.press("f6")  # to focus the url bar
    pyautogui.hotkey("ctrl", "c")  # copy the url of the video
    # press esc twice to focus the video
    pyautogui.press("esc")
    pyautogui.press("esc")

    video_url = pyperclip.paste()
    video_id = getVideoId(video_url)
    duration = get_video_length(video_id)
    duration = duration[0] * 3600 + duration[1] * 60 + duration[2]
    print(duration, 'seconds')

    # timer
    while duration > 0:
        print(f"\r{LCYAN}{duration} second(s)\t{LGREEN}{'▆' * duration:10} ", end="")
        #for k in range(c): print(f"\r{'▆'*c}", end="")
        #if keyboard.read_key() == pauseKey: print("Paused")
        time.sleep(1)
        duration -= 1

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
