import requests

BASE = "http://127.0.0.1:5000/"

response = requests.get(BASE + "/numbers")

print("Status Code: {}, headers: {}".format(response.status_code, response.headers))
print("Response: {}".format(response.json()))
