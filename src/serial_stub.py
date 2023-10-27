# This module provides a dummy replacement for the real serial.Serial class
# Using this class we can stub some data and work with the objects just like
# with real serial ports

class SerialStub:
    def __init__(self, port, baudrate, timeout):
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout

    def timeout(timeout):
        print(f"Serial:: timeout(): {timeout}")

    def open(self):
        print("Serial:: open()")
        pass

    def close(self):
        print("Serial:: close()")
        pass

    def write(self, data):
        print(f"Serial:: write(): {data}")
        pass

    def read(self, size):
        print("Serial:: read()")
        return b'Stub Response\r\n'

    def read_line(self):
        print("Serial:: read_line()")
        pass

    def reset_input_buffer(self):
        print("Serial:: reset_input_buffer()")
        pass

    def reset_output_buffer(self):
        print("Serial:: reset_output_buffer()")
        pass
