#!/usr/bin/env python3
from pydub import AudioSegment
from pydub.playback import play
import os

sound_file = os.path.join(os.getcwd(), 'sounds', 'gunshot.mp3')
if not os.path.exists(sound_file):
    print(f"Error: {sound_file} not found!")
    exit(1)
try:
    sound = AudioSegment.from_mp3(sound_file)
    print("Playing gunshot.mp3...")
    play(sound)
except Exception as e:
    print(f"Error playing sound: {e}")
