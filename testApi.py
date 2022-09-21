import requests
from pprint import pprint

BASE = "http://127.0.0.1:5000/"

response1 = requests.get(BASE + "/numbers/list/20")

print("Status Code: {}, headers: {}".format(response1.status_code, response1.headers))
pprint("Response : {}".format(response1.json()))
