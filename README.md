# disparos-teclado

Inspired by Skkeeper`s https://github.com/skkeeper/linux-clicky script, disparos -teclado produces a gunfire sound each time you press your keyboard. This won't be usefull for anything serious.

Inspired by colszowka's [linux-typewritter](https://github.com/colszowka/linux-typewriter) script, linux-clicky produces a sound everytime you press a key on your keyboard. This might be useful for screensharing or a screencast if you want to have some type of feedback while you type.

## Usage

Run the main.py file and it will automaticly detect your keyboards and start firing rounds as you click.

**Because of the way the script detects the keypresses (by tying itself to the event file in Linux, just like a keylogger would do) it requires root access**

If you are worried about malicious code, just read it.

## Advantages over the original script:

- Gunfire (and python 3).

## Disadvantages

- Requires root access
- It was vibe-coded.

## Dependencies

- Linux (tested under Linux Mint 22.2)
- Python
- pydub
- evdev
- ffmpeg



## License

The code is under the supplied MIT license, therefore it's completely open source.

evdev.py (by Micah Dowty <micah@navi.cx>) is included under the terms of the GPLv2. Thanks to Micah Dowty for writing this module since without it this script would not be possible, or at least not as easy to code.

The keyboard sounds were extracted from ['keyboard-typing’ by Anton](http://www.freesound.org/samplesViewSingle.php?id=137) at Freesound and pixbay.com
