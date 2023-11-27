from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from IN2128HDx import IN2128HDx


# Abstraction for api calls
class Api:
    def __init__(self, projector: IN2128HDx):
        self.projector = projector

        # Add routes to api
        self.router = APIRouter()
        self.router.add_api_route("/api/status", self.get_common_status, methods=["GET"])
        self.router.add_api_route("/api/status/{key}", self.get_status, methods=["GET"])
        self.router.add_api_route("/api/commands/{key}/{subkey}", self.send_command, methods=["GET"])
        self.router.add_api_route("/api/manual-command/{command}", self.send_manual_command, methods=["GET"])

    def get_status(self, key):
        print(f"API::get_status(): {key}")
        return self.projector.get_status(key)

    def get_common_status(self):
        print("API::get_common_status()")
        return self.projector.get_common_status()

    def send_command(self, key: str, subkey: str):
        print(f"API::send_command(): {key}:{subkey}")
        return self.projector.send_command(key, subkey)

    def send_manual_command(self, command: str):
        print(f"API::send_manual_command(): {command}")
        if self.projector.is_command_valid(command):
            return self.projector.send_manual_command(command)
        else:
            return status.HTTP_400_BAD_REQUEST




