import requests
import json

with open("./day_31-40/day_39/creds.json") as f:
    creds = json.load(f)

SHEETY_API = creds['sheety_api']




class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        sheet_response = requests.get(url = SHEETY_API)
        data = sheet_response.json()
        self.destination_data = data['prices']
        return self.destination_data

    def update_destination_data(self):
        for city in self.destination_data:
            new_data = {
                "price" : {
                    "iataCode" : city["iataCode"]
                }
            }

            response = requests.put(
                url = f"{SHEETY_API}/{city['id']}",
                json = new_data
            )
            print(response.text)