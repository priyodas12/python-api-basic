import requests

BASE = "http://127.0.0.1:5000/"

response1 = requests.get(BASE + "/numbers")
response2 = requests.get(BASE + "/persons/priyo")

print("Status Code: {}, headers: {}".format(response1.status_code, response1.headers))
print("Response: {}".format(response1.json()))

print("Status Code: {}, headers: {}".format(response2.status_code, response2.headers))
print("Response: {}".format(response2.json()))
