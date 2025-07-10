from flask import request, Flask
from flask_cors import CORS
import datetime
import json


def loadJson() -> dict:
    with open("track.json", "r") as j:
        data = json.load(j)
        return data


def writeToJson(data):
    with open("track.json", "w") as j:
        json.dump(data, j, indent=4)

server = Flask(__name__)
CORS(server, resources={r"/track.json": {"origins": "*"}})

@server.route('/track.json', methods=["POST"])
def track():
    data = request.get_json()
    print(f"{datetime.datetime.now()} Recieved: {data}")
    localData = loadJson()
    try:
        localData["duration"] += data["duration"]
        writeToJson(localData)
    except Exception:
        print("Something went wrong in updating the json data")
    return 'OK', 200

if __name__ == "__main__":
    server.run(port=5000)