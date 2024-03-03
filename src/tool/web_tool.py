import time

import pyautogui
import pyperclip


def get_html():
    sleep_time = 1
    time.sleep(sleep_time)
    pyautogui.hotkey('ctrl', 'u')
    time.sleep(sleep_time)
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(sleep_time)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(sleep_time)
    pyautogui.hotkey('ctrl', 'w')
    return pyperclip.paste()
