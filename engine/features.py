
from playsound import playsound
import os


# Playing assiatnt sound function
def playAssistantSound():
    music_dir = os.path.join("www", "assets", "audio", "start_sound.mp3")
    playsound(music_dir)
