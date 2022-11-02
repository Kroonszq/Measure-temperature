import requests
import json

URL = "https://api.basecampserver.tech/nodes"
# 'id': 457, 'name': 'jonkologen.1', 'description': 'jonkologen node', 'key': 'Gl1AyMQ2tguwtV7bAMR8oQ
PARAMS = {
    'name': 'jonkologen.1',
    'description': 'jonkologen node',
    'id': 457
}
response = requests.get(URL, params=PARAMS)
response.json()