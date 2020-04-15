import time
import webbrowser
import os
from pynput.mouse import Button, Controller



os.system("python -m pip install pynput --user")
time.sleep(3)

import pynput
from pynput.keyboard import Key, Controller

keyboard = Controller()
mouse = Controller()

#: The play/pause toggle.

media_play_pause = 0

    #: The volume mute button.
media_volume_mute = 0

    #: The volume down button.
media_volume_down = 0
    #: The volume up button.
media_volume_up = 0

    #: The previous track button.
media_previous = 0

    #: The next track button.
media_next = 0

tab = 0

cmd_r = 0

enter = 0

arrow_key_right = 0

print("If a stream is down then manually add one active one!")
webbrowser.open("https://www.twitch.tv/anomaly")
webbrowser.open("https://www.twitch.tv/Mytch")
webbrowser.open("https://www.twitch.tv/pokimane")
webbrowser.open("https://www.twitch.tv/TimTheTatman")

while True:
    keyboard.press(Key.cmd_r)
    keyboard.press(Key.tab)
    keyboard.press(Key.arrow_key_right)
    

