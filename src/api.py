from fastapi import APIRouter
from sercon import SerCon

# Abstraction for api calls
class Api:
    def __init__(self, sercon: SerCon):
        self.sercon = sercon

        self.router = APIRouter()
        self.router.add_api_route("/api/status", self.get_common_status, methods=["GET"])
        self.router.add_api_route("/api/status/{item_id}", self.get_status, methods=["GET"])
        self.router.add_api_route("/api/commands/{key}/{subkey}", self.send_command, methods=["GET"])
        self.router.add_api_route("/api/manual-command/{command}", self.send_manual_command, methods=["GET"])


    def get_status(self, item_id):
        print(f"API::get_status(): {item_id}")
        return self.sercon.get_status(item_id)

    def get_common_status(self):
        print("API::get_common_status()")
        return self.sercon.get_common_status()

    def send_command(self, key: str, subkey: str):
        print(f"API::send_command(): {key}:{subkey}")
        return self.sercon.send_command(key, subkey)

    def send_manual_command(self, command: str):
        print(f"API::send_manual_command(): {command}")
        return self.sercon.send_manual_command(command)


