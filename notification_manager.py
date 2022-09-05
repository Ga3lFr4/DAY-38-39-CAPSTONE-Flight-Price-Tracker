from twilio.rest import Client
import os
from dotenv import load_dotenv
load_dotenv("variables.env")

TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_AUTH = os.getenv("TWILIO_AUTH")
TWILIO_PHONE = "+12184025227"
MY_PHONE = os.getenv("MY_PHONE")

class NotificationManager:

    def send_message(self, price, departure_airport, departure_city, arrival_airport, arrival_city, departure_time, return_time):
        client = Client(TWILIO_SID, TWILIO_AUTH)
        message = client.messages \
        .create(
            to=MY_PHONE,
            from_=TWILIO_PHONE,
            body=f"Low price alert! Only £{price} to fly from {departure_city}-{departure_airport} to"
                 f" {arrival_city}-{arrival_airport}, from {departure_time} to {return_time}"
        )
        print(message.status)
