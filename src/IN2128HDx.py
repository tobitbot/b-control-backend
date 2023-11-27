# Serial Connector
from dicts import Commands, VideoSources
from sercon import SerCon
import re

COMMAND_REGEX = "r'^\([A-Za-z]{3}(\?|\d{1,4})\)$'"

# Abstraction for infocus 2128HDx projector
class IN2128HDx:
  def __init__(self, sercon: SerCon):
    self.sercon = sercon
    self.command_validator = re.compile(COMMAND_REGEX)

  # Validates the given command
  # @return a boolean
  def is_command_valid(self, command: str):
    return self.command_validator.match(command)

  # Loads the common status for the beamer
  def get_common_status(self):
    # Get power status
    status = {}

    try:
      # b'(0-1,1)'
      status["power"] = self._send_command_and_read(Commands["power"]["val"])["value"]

      # b'(0-1,0)'
      status["autosource"] = self._send_command_and_read(Commands["autosource"]["val"])["value"]

      # b'(0-22,4)'
      status["source"] = self._get_video_source(self._send_command_and_read(Commands["source"]["val"])["value"])

      # b'(0-1,1)'
      status["blank"] = self._send_command_and_read(Commands["blank"]["val"])["value"]

      # b'(0-10,0)'
      status["volume"] = self._send_command_and_read(Commands["volume"]["val"])["value"]

      status["brightness"] = self._send_command_and_read(Commands["brightness"]["val"])["value"]

      # b'(0-65535,107)'
      status["lamphours"] = self._send_command_and_read(Commands["lamphours"]["val"])["value"]

      # b'("5000")'
      lamphours: str = self._send_command_and_read(Commands["maxlamphours"]["val"])["range"]
      status["maxlamphours"] = lamphours.strip('"')
    except:
      print("Exception getting common status")
    return status

  # Gets the status for the given key
  # @return {key: value}
  def get_status(self, key: str):
    response = self._send_command_and_read(Commands[key]["val"])

    if key == "source":
      response.set_value(self._get_video_source(response))

    return {key: response}

  # Sends the command for the given keys
  def send_command(self, key: str, subkey: str):
    response = self._send_command_and_read(Commands[key][subkey])
    if key == "source":
      response["value"] = self._get_video_source(response["value"])

    return response

  # Sends the given command
  def send_manual_command(self, command: str):
    return self._send_command_and_read(command)



  #############################
  # Private methods
  #############################

  # Sends a command and gets the answer as Response
  # @return an Response object
  def _send_command_and_read(self, status_command: str):
    resp = Response(self.sercon.send_and_read(status_command))
    return resp.get()

  #
  #
  def _get_video_source(self, val: int):
    try:
      return VideoSources[val]
    except:
      return 0

# Helper class to wrap up a response from projector
class Response:
  # Given a form of ['0-1', '0']
  def __init__(self, response: str):
    self.response: response

    self.range = ""
    self.value = ""

    self._split_result(response)

  def get_range(self):
    return self.range

  def get_value(self):
    return self.value

  def set_value(self, val):
    self.val = val

  def get(self):
    json = {}
    json["result"] = "ok"
    json["range"] = self.range
    json["value"] = self.value
    return json

  def _split_result(self, response: str):
    resp = response.strip("(").strip(")").split(",")

    if len(resp) == 1:
       self.range = resp[0]
    elif len(resp) == 2:
       self.range = resp[0]
       self.value = int(resp[1])