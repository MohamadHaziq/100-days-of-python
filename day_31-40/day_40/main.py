#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
import datetime as dt

ORIGIN_CITY_IATA = "LON"

data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

sheet_data = data_manager.get_destination_data()
# sheet_data = [
#     {'city': 'Paris', 'iataCode': 'PAR', 'lowestPrice': 54, 'id': 2},
#     {'city': 'Berlin', 'iataCode': 'BER', 'lowestPrice': 42, 'id': 3},
#     {'city': 'Tokyo', 'iataCode': 'TYO', 'lowestPrice': 485, 'id': 4},
#     {'city': 'Sydney', 'iataCode': 'SYD', 'lowestPrice': 551, 'id': 5},
#     {'city': 'Istanbul', 'iataCode': 'IST', 'lowestPrice': 95, 'id': 6},
#     {'city': 'Kuala Lumpur', 'iataCode': 'KUL', 'lowestPrice': 414, 'id': 7}, 
#     {'city': 'New York', 'iataCode': 'NYC', 'lowestPrice': 240, 'id': 8}, 
#     {'city': 'San Francisco', 'iataCode': 'SFO', 'lowestPrice': 260, 'id': 9}, 
#     {'city': 'Cape Town', 'iataCode': 'CPT', 'lowestPrice': 378, 'id': 10}
# ]

if sheet_data[0]['iataCode'] == '':
    flight_search = FlightSearch()

    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row['city'])
    
    print(sheet_data)

    data_manager.destination_data = sheet_data
    data_manager.update_destination_data()

tomorrow = dt.datetime.now() + dt.timedelta(days=1)
six_month_from_today = dt.datetime.now() + dt.timedelta(days=(6 * 30))

for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )

    if flight is None:
        continue
    
    if flight.price < destination['lowestPrice']:

        users = data_manager.get_customer_emails()
        emails = [row["email"] for row in users]
        names = [row["firstName"] for row in users]

        message = (
            f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."           
        )
        
        if flight.stop_overs > 0:
            message += f"Flight has {flight.stop_overs} stop over. via {flight.via_city}"
            # print (message)

        link = f"https://www.google.co.uk/flights?hl=en#flt={flight.origin_airport}.{flight.destination_airport}.{flight.out_date}*{flight.destination_airport}.{flight.origin_airport}.{flight.return_date}"
    
        # notification_manager.send_emails(email, message, link)
        print (emails, message, link)