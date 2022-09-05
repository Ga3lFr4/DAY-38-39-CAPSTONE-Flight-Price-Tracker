#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program
# requirements.
from data_manager import DataManager
from notification_manager import NotificationManager
from pprint import pprint

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()

if sheet_data[0]["iataCode"] == '':
    from flight_search import FlightSearch
    flight_search = FlightSearch()
    for row in sheet_data:
        row["iataCode"] = flight_search.find_iata_code(row["city"])

data_manager.destination_data = sheet_data
data_manager.update_iata_code()

for row in sheet_data:
    from flight_search import FlightSearch
    flight_search = FlightSearch()
    flight_search.find_flights(row["iataCode"])
    if flight_search.price < sheet_data[0]["lowestPrice"]:
        notification_manager = NotificationManager()
        notification_manager.send_message(flight_search.price, flight_search.departure_airport, flight_search.departure_city,
                                      flight_search.arrival_airport, flight_search.arrival_city, flight_search.out_date, flight_search.return_date)
    else:
        print("No good deal")
    # print(f"{flight_search.arrival_city} - {flight_search.arrival_airport}: £{flight_search.price}")


