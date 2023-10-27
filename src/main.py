# Main file for this project. Start with:
#  run with: 'uvicorn main:app --port 8000 --reload'
#
#

import serial
from fastapi import FastAPI

# Import own modules
from sercon import SerCon
from api import Api

# Define constants
SERIAL_PORT_0 = "/dev/ttySC0"
SERIAL_PORT_1 = "/dev/ttySC1" # Not used
BAUDRATE = 9600
PARITY = serial.PARITY_NONE
STOP_BITS = serial.STOPBITS_TWO
BYTESIZE = serial.EIGHTBITS
SER_RESP_TIMEOUT = 1


#######################
# Program starts here #
#######################

print("Starting b-control-backend...")

# Create serial connection
sercon = SerCon(SERIAL_PORT_0, BAUDRATE, PARITY, STOP_BITS, BYTESIZE, SER_RESP_TIMEOUT)
sercon.init()

status = sercon.get_common_status()
print(status)

# Start api
app = FastAPI()
api = Api(sercon)
app.include_router(api.router)

