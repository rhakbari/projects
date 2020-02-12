"""One way Messaging app"""

from twilio.rest import Client
import json
from flask import Flask, jsonify

app = Flask(__name__)

# Your Account SID from twilio.com/console
ACCOUNT_SID = "ACb389df318e66cfb10ff8bc8992633581"
# Your Auth Token from twilio.com/console
AUTH_TOKEN = "5b46d9b0afff17cd89ccb966ef4c0658"


@app.route("/send/whatsapp/03183339148")
def send_whatapp():
    client = Client(ACCOUNT_SID, AUTH_TOKEN)

    message = client.messages.create(
        from_="whatsapp:+14155238886",
        body="Hello, there! Raza here :)",
        to="whatsapp:+923183339148",
    )

    return jsonify({"message": "whatsapp sent"})


@app.route("/send/text/03183339148")
def send_text():

    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages.create(
        body="Raza here, trying to send text via python script",
        from_="+17029792063",
        to="+923183339148",
    )

    return jsonify({"message": "text sent"})
