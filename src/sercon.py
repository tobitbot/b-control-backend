# Serial Connector
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

  # Sends the given command
  def send_manual_command(self, command: str):
    return self.send_and_read(command)

  # Create a valid command
  def send_and_read(self, string):
    self.ser_port.write(str.encode(string + "\r\n"))
    response = self.ser_port.read(20)

    if response == "?" or response == "":
      print(f"ERROR: Error processing command {string}")

    return response.decode() # Or some self defined error code