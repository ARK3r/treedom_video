# the link: https://www.instagram.com/p/BwUkFO2nmTn/

from pynput.keyboard import Key, Controller
import time

keyboard = Controller()

weNEEDmoreTREES = True

while weNEEDmoreTREES:
    # 3 seconds required to add a view to an instagram view
    time.sleep(10)

    # refresh page
    keyboard.press(Key.f5)
    keyboard.release(Key.f5)

    # wait for page to load
    time.sleep(3)

    # i couldn't find a key to start the video instantly
    # so i just click tab to select over the video and i
    # counted and it was 7
    for i in range(7):

        # leave some time between the tabs
        time.sleep(0.8)
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)

    # play the video
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

    # and the loop is over, you got 0.001 of a tree planted
