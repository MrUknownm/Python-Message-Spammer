# MODULES
import pyautogui
import webbrowser
import time
import colorama
colorama.init()

message = input("\033[1;34mWhat message do you want to keep sending? \033[0m")
repeats = int(input("\033[1;34mHow many times do you want to spam?  \033[0m"))
delay = int(input("\033[1;34mHow many milliseconds do you want to wait in between each message?  \033[0m"))

isLoaded = input("\033[1;34mPress Enter when your messaging app is loaded up.\033[0m")

print("\033[1;34mYou have five seconds to refocus the text input area of your messaging app\033[0m")
time.sleep(5)

# SPAM
for i in range(0, repeats):
    if message != "":
        pyautogui.typewrite(message)
        pyautogui.press("enter")
    else:
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press("enter")

    time.sleep(delay / 1000)

print("\033[1;34mDone\n\033[0m")

input("\033[1;34mPress Anything to exit...\033[0m")
