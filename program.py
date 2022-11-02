import requests


URL = "https://api.agify.io?name=meelad"
PARAMS = {"name": "meelad"}
response = requests.get(URL, PARAMS)

if response.status_code != 200:
    exit("Something went wrong")




