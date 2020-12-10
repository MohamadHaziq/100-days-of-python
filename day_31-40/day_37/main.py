import requests

USERNAME = "username"
TOKEN = "generate_token"

pixela_endpoint = "https://pixe.la/v1/users"
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
pixel_send = f"{pixela_endpoint}/{USERNAME}/graphs/testgraph"
user_params = {
    "token" : "generate_token",
    "username" : "username",
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes",
}

# response = requests.post(url = pixela_endpoint, json = user_params)

graph_config = {
    "id" : "testgraph",
    "name" : "TestGraph",
    "unit" : "Times",
    "type" : "float",
    "color" : "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

pixel_config = {
    "date" : "20201210",
    "quantity" : "20"
}
# response = requests.post(url = graph_endpoint, json = graph_config, headers = headers)
response = requests.post(url = pixel_send, json = pixel_config, headers = headers)

print (response.text)
