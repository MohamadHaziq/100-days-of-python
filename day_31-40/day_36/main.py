import requests
import json
from twilio.rest import Client

with open('./day_31-40/day_36/creds.json') as file:
    creds = json.load(file)

API_KEY = creds['api_key']
NEWS_API_KEY = creds['news_api']
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

TWILIO_ACCOUNT_SID = creds['TWILIO_ACCOUNT_SID']
TWILIO_AUTH_TOKEN = creds['TWILIO_AUTH_TOKEN']

stock_params = {
    "function" : "TIME_SERIES_DAILY",
    "symbol" : STOCK_NAME,
    "apikey" : API_KEY,
}

news_params = {
    "qInTitle" : COMPANY_NAME,
    "apiKey" : NEWS_API_KEY
}

response = requests.get(STOCK_ENDPOINT, params = stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key,value) in data.items()]

yesterday = data_list[0]
yesterday_closing_price = yesterday["4. close"]

day_before_yesterday = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday["4. close"]

difference = abs(float(yesterday_closing_price) - float(day_before_yesterday_closing_price))
diff_percent = (difference / float(yesterday_closing_price) * 100)

print(diff_percent)

if diff_percent > 1:
    print ("News Time !")

    response = requests.get(NEWS_ENDPOINT, news_params)
    data = response.json()
    articles = data['articles'][:3]

    formatted_articles = [f"Headline: {article['title']} \nBrief: {article['description']}" for article in articles]
    
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    for article in formatted_articles:
        message = client.messages \
                        .create(
                            body=article,
                            from_='+17658964901',
                            to='INSERT NUMBER HERE'
                        )

        print(message.status)


#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

