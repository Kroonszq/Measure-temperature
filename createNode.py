import requests
import json

URL = "https://api.basecampserver.tech/nodes"
HEADERS = {'Content-Type': 'application/json'}
DATA = {
    'name': 'jonkologen.1',
    'description': 'jonkologen node',
}

try:
    response = requests.post(URL, data=json.dumps(DATA), headers=HEADERS, timeout=1)
    print(response.json())
except requests.exceptions.Timeout:
    print("Request timed out")


#{'id': 457, 'name': 'jonkologen.1', 'description': 'jonkologen node', 'key': 'Gl1AyMQ2tguwtV7bAMR8oQ'}

