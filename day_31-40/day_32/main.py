import smtplib
import pandas as pd
import datetime as dt
import json
import random

with open("./day_31-40/day_32/creds.json") as f:
    creds = json.load(f)
    my_email = creds['email']
    my_pass = creds['password']
    destination = creds['destination']

##################### Starting Project ######################

now = dt.datetime.now()
today = (now.month, now.day)

data = pd.read_csv("./day_31-40/day_32/birthdays.csv")
birthdays_dict = {(row['month'], row['day']): row for (idx, row) in data.iterrows()}

if today in birthdays_dict:
    birthday_person = birthdays_dict[today]
    print("Yep")

    with open(f'./day_31-40/day_32/letter_templates/letter_{random.randint(1,3)}.txt') as f:
        contents = f.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user = my_email, password = my_pass)
    connection.sendmail(from_addr = my_email,
                        to_addrs = birthday_person['email'], 
                        msg = f"Subject: Happy Birthday \n\n {contents}")
