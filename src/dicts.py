from enum import Enum

# Dictonary to define all api commands to rs232 commands
Commands = {
  "autosource": {
    "val": "(ASC?)",
    "on": "(ASC1!)",
    "off": "(ASC0!)"
  },
  "blank": {
    "val": "(BLK?)",
    "on": "(BLK1!)",
    "off": "(BLK0!)"
  },
  "power": {
    "val": "(PWR?)",
    "on":  "(PWR1!)",
    "off": "(PWR0!)"
  },
  "source": {
    "val": "(SRC?)",
    "prev": "(SRC-!)",
    "next": "(SRC+!)",
    "hdmi": "(SRC4!)"
  },
  "volume": {
    "val": "(VOL?)",
    "mute": "(VOL0!)",
    "up": "(VOL+!)",
    "down": "(VOL-!)"
  },
  "lamphours": {
    "val": "(LMP?)",
  },
  "maxlamphours": {
    "val": "(LIF?)",
  },
  "brightness": {
    "val": "(BRT?)",
    "up": "(BRT+!)",
    "down": "(BRT-!)",
    "full": "(BRT100!)"
  }
}

VideoSources = {
  1: "Computer 1",
  2: "Computer 2",
  4: "HDMI",
  11: "Video",
  12: "S-Video"
}
