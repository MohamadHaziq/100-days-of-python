from twilio.rest import Client
import json

with open("./day_31-40/day_39/creds.json") as f:
    creds = json.load(f)

TWILIO_SID = creds['TWILIO_ACCOUNT_SID']
TWILIO_AUTH_TOKEN = creds['TWILIO_AUTH_TOKEN']
TWILIO_VIRTUAL_NUMBER = creds['TWILIO_VIRTUAL_NUMBER']
TWILIO_VERIFIED_NUMBER = creds['TWILIO_VERIFIED_NUMBER']


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body = message,
            from_ = TWILIO_VIRTUAL_NUMBER,
            to = TWILIO_VERIFIED_NUMBER,
        )

        print (message.sid)
    