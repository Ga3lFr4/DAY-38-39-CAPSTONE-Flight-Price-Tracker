from pprint import pprint
import requests
import os
from dotenv import load_dotenv
load_dotenv('variables.env')

SHEETY_PRICES_ENDPOINT = os.getenv('SHEETY_PRICES_ENDPOINT')
SHEETY_EMAIL_ENDPOINT = os.getenv('SHEETY_EMAIL_ENDPOINT')
SHEETY_AUTH = {
    "Authorization": os.getenv('SHEETY_AUTH')
}


class DataManager:

    def __init__(self):
        self.destination_data = {}
        self.first_name = ""
        self.last_name = ""
        self.email_1 = ""
        self.email_2 = ""
        self.email_list = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers=SHEETY_AUTH)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)

    def create_user(self):
        print("Welcome to flight club, please enter email and name \n")
        self.first_name = input("What's your first name ? \n")
        self.last_name = input("What's your last name? \n")
        self.email_1 = input("What's your email ? \n")
        self.email_2 = input("Please confirm your email \n")
        if self.email_1 == self.email_2:
            return True
        return False

    def add_user_to_database(self):
        params = {
            "user": {
                "firstName": self.first_name,
                "lastName": self.last_name,
                "email": self.email_1
            }
        }
        response = requests.post(url=SHEETY_EMAIL_ENDPOINT, headers=SHEETY_AUTH, json=params)
        response.raise_for_status()


    def get_emails(self):
        response = requests.get(url=SHEETY_EMAIL_ENDPOINT, headers=SHEETY_AUTH)
        data = response.json()
        self.email_list = data["users"]
        return self.email_list
