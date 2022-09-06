from twilio.rest import Client
import os
from dotenv import load_dotenv
import smtplib
load_dotenv("variables.env")

TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_AUTH = os.getenv("TWILIO_AUTH")
TWILIO_PHONE = "+12184025227"
MY_PHONE = os.getenv("MY_PHONE")
EMAIL= os.getenv('GMAIL_ADDR')
PW = os.getenv('GMAIL_PW')

class NotificationManager:
    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_PHONE,
            to=MY_PHONE,
        )
        # Prints if successfully sent.
        print(message.sid)

    def send_emails(self, message, url, email):
        with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=EMAIL, password=PW)
            final_message = message + "\n" + url
            connection.sendmail(msg=f"Subject:New cheap flight!\n\n{final_message}".encode("utf-8"), from_addr=EMAIL, to_addrs=email)

