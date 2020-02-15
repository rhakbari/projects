"""One way Messaging app"""

from twilio.rest import Client
from twilio.twiml.messaging_response import Body, Message, Redirect, MessagingResponse
import json
from flask import Flask, jsonify, request

app = Flask(__name__)

# Your Account SID from twilio.com/console
ACCOUNT_SID = "account_sid"
# Your Auth Token from twilio.com/console
AUTH_TOKEN = "auth_token"
# Sender's phone number
sender_num ="+921234567890: "
# Twilio bot phone number 
bot_num = "+14155238886: "

@app.route("/whatsapp")
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
        body=request.values.get('From', None)+": "+request.values.get('Body', None),
        from_="+18577634315",
        to="+923432918501",
        )

    #receiving sms from phone number
    message = client.messages.create(
        body=request.values.get('Body', None),
        from_="+18577634315",
        to="+whatsapp:+923183339148",
    )

    message = client.messages.create(
        body=request.values.get('Body', None),
        from_="whatsapp:+14155238886",
        to="+whatsapp:+923183339148",
    )

    return jsonify({"message": "sms sent"})


if __name__ == "__main__":
    app.run(port=5000)
