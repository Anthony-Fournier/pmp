# Anthony David Fournier    Project Started 11/22/2021
# A personal project for an acceptable music playing assistant

# Local test file /home/tony/Music/Sublime/40oz. To Freedom [Explicit]/10 - Scarlet Begonias.mp3


# Import modules
from pygame import mixer
from time import sleep

# Basic Functions
# Initialize mixer
mixer.init()

# Play file 
mixer.music.load('/home/tony/Music/Sublime/40oz. To Freedom [Explicit]/10 - Scarlet Begonias.mp3')


mixer.music.play()

while mixer.music.get_busy():
    sleep(1)

print ("done")

# Pause playback

# Resume playback

# Stop playback

# Add file to list

# Remove file from list
