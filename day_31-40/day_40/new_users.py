import requests
import json

with open("./day_31-40/day_40/creds.json") as f:
    creds = json.load(f)

SHEETY_API = creds['sheety_users_api']

print ("Welcome to Flight Club")
print ("We find you the best of the best")

first_name = input("What is your first name?\n")
last_name = input("What is your last name?\n")
email = input("What is your email address?\n")
email_check = input("Type your email again.\n")

user_params = {
    "user" : {
        'firstName' : first_name,
        'lastName' : last_name,
        'email' : email
    }
}

print (user_params)

if email_check == email:
    print ("Welcome to the club !")
    response = requests.post(url = SHEETY_API, json = user_params)
    print (response.text)

else:
    print ("Please try again later")
