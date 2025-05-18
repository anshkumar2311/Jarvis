import os

import eel

from engine.features import *

eel.init("www")
playAssistantSound()

os.system('xdg-open chrome "http://localhost:8080/index.html"')  #in place of xdg-open use start in windows

eel.start('index.html', mode=None , host='localhost', block=True)
