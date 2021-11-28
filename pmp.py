# Anthony David Fournier    Project Started 11/22/2021
# A personal project for an acceptable music playing assistant

# Local test file /home/tony/Music/Sublime/40oz. To Freedom [Explicit]/10 - Scarlet Begonias.mp3
testSong = '/home/tony/Music/Sublime/40oz. To Freedom [Explicit]/10 - Scarlet Begonias.mp3'

# Import modules
from pygame import mixer, time

# Initialize mixer
mixer.init()

# Basic Functions


# Play Music Function 
def play(file):
    mixer.music.load(file)
    mixer.music.play()
    print(f"Now Playing: {file}")
    while mixer.music.get_busy():
        time.Clock().tick()

# Pause/Resume Playback Function
def pause():
    if mixer.music.get_busy():
        mixer.pause()
        print(f"Now Paused: {file}")
    else:
        mixer.unpause()
        print(f"Resumed Playing: {file}")

# Stop Playback Function
def stop():
    mixer.music.stop()

# Add file to list

# Remove file from list

# Quit Program
def quitPmp():
    mixer.quit()
    exit(0)

# MAIN LOOP

# args of pmp play,(file)/add,(file)/pause/stop

# some kind of update(dt) loop? -- doesnt really make sense
# checking for input commands
playMusic(testSong)

