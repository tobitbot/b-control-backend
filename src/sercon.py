# Serial Connector
from dicts import commands
import serial, serial_stub, os

# Abstraction for serial connection to beamer
class SerCon:
  def __init__(self, port: str, baudrate: int, parity: int, stopbits: float, bytesize: int, timeout: int):
    self.port = port
    self.baudrate = baudrate
    self.parity = parity
    self.stopbits = stopbits
    self.bytesize = bytesize
    self.timeout = timeout

    print(f"PARAMS: {self.port}, {self.baudrate}, {self.parity}, {self.stopbits}, {self.bytesize}, {self.timeout}")

    # Check serial port
    if os.path.exists(self.port):
      print("Interface exists, use real serial port")
      self.ser_port = serial.Serial(
        self.port,
        self.baudrate,
        self.bytesize,
        self.parity,
        self.stopbits,
        self.timeout
        )
    else:
      print("Interface does not exists, use fake serial port")
      self.ser_port = serial_stub.SerialStub(self.port, self.baudrate, self.timeout)


  # Loads the common status for the beamer
  def get_common_status(self):
    # Get power status
    status = {}
    status["power"] = self._send_and_read(commands["power"]["val"])
    status["autosource"] = self._send_and_read(commands["autosource"]["val"])
    status["source"] = self._send_and_read(commands["source"]["val"])
    status["blank"] = self._send_and_read(commands["blank"]["val"])
    status["volume"] = self._send_and_read(commands["volume"]["val"])
    status["lamphours"] = self._send_and_read(commands["lamphours"]["val"])
    status["maxlamphours"] = self._send_and_read(commands["maxlamphours"]["val"])
    return status

  # Gets the status for the given key
  def get_status(self, key: str):
      return self._send_and_read(commands[key]["val"])

  # Sends the command for the given keys
  def send_command(self, key: str, subkey: str):
    return self._send_and_read(commands[key][subkey])

  # Sends the given command
  def send_manual_command(self, command: str):
    return self._send_and_read(command)


  # private methods

  # Create a valid command
  def _send_and_read(self, string):
    self.ser_port.write(str.encode(string + "\r\n"))
    response = self.ser_port.read(10)
    if response == "?" or response == "":
      print(f"ERROR: Error processing command {string}")

    return response.decode() # Or some self defined error code