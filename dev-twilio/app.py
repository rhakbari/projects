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

@app.route("/sms")
# def send_whatapp():
def sms_reply():
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages.create(
        body=bot_num+"hi this is a test sms", # <number> : <message> format
        from_="whatsapp:+14155238886", # twilio bot phone number
        to="whatsapp:phone number",
    )
    return jsonify({"message": "whatsapp sms sent"})

# Forwards the message from whatsapp to the phone number via SMS

@app.route("/whatsappsms", methods=["GET", "POST"])
def send_text():

    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    resp = MessagingResponse()
    message = client.messages.create(
        body="Your message has been sent",
        from_="whatsapp:+14155238886", # twilio bot phone number
        to="whatsapp:phone number",
    )
    message = client.messages.create(

        body=sender_num+request.values.get('Body', None), # <number> : <message> formats
        from_="phone number",  # Registered number from twilio 
        to="phone number",
    )

    return jsonify({"message": "sms sent"})


if __name__ == "__main__":
    app.run(port=5000)
