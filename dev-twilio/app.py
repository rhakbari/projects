"""One way Messaging app"""

from twilio.rest import Client
from twilio.twiml.messaging_response import Body, Message, Redirect, MessagingResponse
import json
from flask import Flask, jsonify, request

app = Flask(__name__)

# Your Account SID from twilio.com/console
ACCOUNT_SID = "ACfd245978f13be3b6c22999b046fb6a6a"
# Your Auth Token from twilio.com/console
AUTH_TOKEN = "3604bdb5409028009cfc5298cb9e4dbf"

sender_num = "+923183339148: "
bot_num = "+14155238886: "

@app.route("/sms")
# def send_whatapp():
def sms_reply():
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages.create(
        body=bot_num+"hi this is a test sms",
        from_="whatsapp:+14155238886",
        to="whatsapp:+923183339148",
    )
    return jsonify({"message": "whatsapp sms sent"})


@app.route("/whatsappsms", methods=["GET", "POST"])
def send_text():

    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    resp = MessagingResponse()
    message = client.messages.create(
        body="Your message has been sent",
        from_="whatsapp:+14155238886",
        to="whatsapp:+923183339148",
    )
    message = client.messages.create(

        body=sender_num+request.values.get('Body', None),
        from_="+18577634315",
        to="+923432918501",
    )

    return jsonify({"message": "sms sent"})


if __name__ == "__main__":
    app.run(port=5000)
