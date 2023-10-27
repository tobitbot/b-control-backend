from enum import Enum

# Dictonary to define all api to rs232 commands
commands = {
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
  }
}


# Video sources
Sources = Enum("Sources", ["Computer 1", "Computer 2", "S-VIDEO"])

class Sources:
  Computer_1 = 1
  Computer_2 = 2
  HDMI = 4
  Video = 11
  S_Video = 12
