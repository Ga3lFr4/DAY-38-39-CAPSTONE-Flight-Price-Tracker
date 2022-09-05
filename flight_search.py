from data_manager import DataManager
import requests
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv
load_dotenv("variables.env")

now = datetime.now()

tomorrow = now + timedelta(days=1)
tomorrow = tomorrow.strftime("%d/%m/%Y")

six_months = now + timedelta(days=180)
six_months = six_months.strftime("%d/%m/%Y")

seven_days = now + timedelta(days=7)
seven_days = seven_days.strftime("%d/%m/%Y")

twentyeight_days = now + timedelta(days=28)
twentyeight_days = twentyeight_days.strftime("%d/%m/%Y")

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com/locations/query"

TEQUILA_KEY = {
    "apikey": os.getenv('TEQUILA_API'),
    "Accept": "application/json",
}


class FlightSearch:

    def __init__(self):
        self.price = 0
        self.departure_airport = ""
        self.departure_city = ""
        self.arrival_airport = ""
        self.arrival_city = ""
        self.out_date = ""
        self.return_date = ""

    def find_iata_code(self, city):
        params = {
            "term": city
        }
        response = requests.get(url=TEQUILA_ENDPOINT, headers=TEQUILA_KEY, params=params)
        data = response.json()
        code = data["locations"][0]["code"]
        return code

    def find_flights(self, code):
        params = {
            "fly_from": "LON",
            "fly_to": code,
            "date_from": tomorrow,
            "date_to": six_months,
            "return_from": seven_days,
            "return_to": twentyeight_days,
            "flight_type": "round",
            "curr": "GBP",
            "max_stopovers": 0
        }
        response = requests.get(url="https://tequila-api.kiwi.com/v2/search", headers=TEQUILA_KEY, params=params)
        data = response.json()["data"]
        self.price = data[0]["price"]
        self.departure_airport = data[0]["flyFrom"]
        self.departure_city = data[0]["cityFrom"]
        self.arrival_city = data[0]["cityTo"]
        self.arrival_airport = data[0]["flyTo"]
        self.out_date = data[0]["route"][0]["local_departure"].split("T")[0],
        self.return_date = data[0]["route"][1]["local_departure"].split("T")[0]
