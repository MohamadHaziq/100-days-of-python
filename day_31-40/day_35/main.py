import requests
import json
from twilio.rest import Client

with open("./day_31-40/day_35/creds.json") as file:
    creds = json.load(file)

MY_LAT = 3.139003
MY_LONG = 101.686852

account_sid = creds['TWILIO_ACCOUNT_SID']
auth_token = creds['TWILIO_AUTH_TOKEN']
api_key = creds['openweather']
OWM_endpoint = "https://api.openweathermap.org/data/2.5/onecall"

weather_params = {
    "lat" : MY_LAT,
    "lon" : MY_LONG,
    "appid" : api_key,
    "exclude" : "current,minutely,daily"
}

response = requests.get(OWM_endpoint, params = weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data['hourly'][:12]


will_rain = False

for hour_data in weather_slice:
    condition_code = (hour_data['weather'][0]['id'])
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                        body="Bring umbrella",
                        from_='+17658964901',
                        to='INSERT NUMBER'
                    )

    print(message.status)