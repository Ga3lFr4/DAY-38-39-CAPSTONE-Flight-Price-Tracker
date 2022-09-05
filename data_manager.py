import requests
import os
from dotenv import load_dotenv
load_dotenv("variables.env")

SHEETY_ENDPOINT = os.getenv("SHEETY_ENDPOINT")

SHEETY_AUTH = {
    "Authorization": os.getenv("SHEETY_AUTH"),
}


class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        sheet_request = requests.get(url=SHEETY_ENDPOINT, headers=SHEETY_AUTH)
        self.destination_data = sheet_request.json()["prices"]
        return self.destination_data

    def update_iata_code(self):
        for city in self.destination_data:
            row_id = city["id"]
            iata_code = city["iataCode"]
            params = {
                "price": {
                    'iataCode': iata_code
                }
            }
            requests.put(url=f"https://api.sheety.co/8ea934c3704cc59f230f19922252c500/flightDeals/prices/{row_id}", headers=SHEETY_AUTH, json=params)