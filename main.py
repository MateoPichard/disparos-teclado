#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Fábio André Damas <skkeeper at gmail dot com>
# Modified for gunshot.wav and reload.wav by Mateo Pichard

import os
import sys
import threading
from pydub import AudioSegment
from pydub.playback import _play_with_ffplay as play
from evdev import InputDevice, ecodes, list_devices
from optparse import OptionParser
from signal import signal, SIGINT

# Handle CTRL+C
def signal_handler(sig, frame):
    print("\033[1;32mCTRL + C Detected. Exiting ...\033[0m")
    sys.exit(0)
signal(SIGINT, signal_handler)

# Handle arguments
parser = OptionParser()
parser.add_option(
    '-v', '--volume', action="store", dest='volume',
    help="sets the volume of the sound (0.0 to 2.0, 1.0 is default)",
    type="float", default=1.0)
(options, args) = parser.parse_args()

# Paths to sound files
sound_files = {
    "default": os.path.join(os.getcwd(), 'sounds', 'gunshot.wav'),
    "reload": os.path.join(os.getcwd(), 'sounds', 'reload.wav')
}

# Check if sound files exist
for key, path in sound_files.items():
    if not os.path.exists(path):
        print(f"\033[1;31mError: {path} not found!\033[0m")
        sys.exit(1)

# Load sounds
try:
    default_sound = AudioSegment.from_wav(sound_files["default"])
    reload_sound = AudioSegment.from_wav(sound_files["reload"])
    print("Sounds loaded successfully!")
except Exception as e:
    print(f"\033[1;31mError loading sound files: {e}\033[0m")
    sys.exit(1)

# Adjust volume (pydub uses dB, convert volume to dB scale)
default_sound = default_sound + (20 * (options.volume - 1))
reload_sound = reload_sound + (20 * (options.volume - 1))

# Define letter key codes (A-Z)
letter_codes = set(range(16, 26)) | set(range(30, 39)) | set(range(44, 51))  # Q-W-E-R-T-Y-U-I-O-P, A-S-D-F-G-H-J-K-L, Z-X-C-V-B-N-M

# Detect keyboards
def detect_keyboards():
    devices = [InputDevice(path) for path in list_devices()]
    keyboards = [dev for dev in devices if ecodes.EV_KEY in dev.capabilities()]
    if not keyboards:
        print("\033[1;31mNo keyboards detected!\033[0m")
        print("Available devices:")
        for dev in devices:
            print(f"Name: {dev.name}, Path: {dev.path}")
        sys.exit(1)
    else:
        print("Keyboards detected:")
        for kb in keyboards:
            print(f"Name: {kb.name}, Path: {kb.path}")
    return keyboards

# Play sound in a separate thread to avoid blocking
def play_sound(sound):
    threading.Thread(target=play, args=(sound,), daemon=True).start()

# Main loop
keyboards = detect_keyboards()
keyboards = [kb for kb in keyboards if "AT Translated Set 2" in kb.name]
if not keyboards:
    print("\033[1;31mNo AT Translated Set 2 keyboard found!\033[0m")
    sys.exit(1)

try:
    for device in keyboards:
        print(f"Listening on {device.name} ({device.path})")
        for event in device.read_loop():
            if event.type == ecodes.EV_KEY and event.value == 1:  # Key press
                key_name = ecodes.KEY.get(event.code, 'Unknown')
                print(f"Key pressed: {event.code} ({key_name})")
                try:
                    if event.code in letter_codes:
                        print("Playing gunshot.wav...")
                        play_sound(default_sound)
                    elif event.code in ecodes.KEY:
                        print("Playing reload.wav...")
                        play_sound(reload_sound)
                except Exception as e:
                    print(f"\033[1;31mError playing sound: {e}\033[0m")
except Exception as e:
    print(f"\033[1;31mError: {e}\033[0m")
