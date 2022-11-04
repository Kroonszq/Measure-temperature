import requests
import time
import json
from sense_hat import SenseHat
from datetime import datetime

sense = SenseHat()

URL: str = "https://api.basecampserver.tech/sensors?key=Gl1AyMQ2tguwtV7bAMR8oQ"

def uploadData(timestamp, temperature, humidity, pressure):
    DATA = {
        "timestamp": round(int(timestamp),2),
        "temperature": round(temperature,2),
        "humidity": round(humidity,2),
        "pressure": round(pressure,2),
    }

    print(DATA)

    while True:
        try:
            res = requests.post(url=URL, data=json.dumps(DATA), headers={"Content-Type": "application/json", "accept": "application/json"})
            print(f"Data uploaded to the server")
            print(res.status_code)
            break
        except requests.exceptions.Timeout as e:
            print(e)
            continue
        except requests.exceptions.HTTPError as x:
            print(x)
            exit("Something went terribly wrong :(")

def time_stamp():
    return time.time()

def get_temperature():
    while True:
        t = sense.get_temperature()
        h = str(t)
        sense.show_message(str(h), scroll_speed=0.05)

        return t

def get_pressure():
    while True:
        p = sense.get_pressure()
        h = str(p)
        sense.show_message(str(h), scroll_speed=0.05)

        return p

def get_humidity():
    while True:
        h = sense.get_humidity()
        y = str(h)
        sense.show_message(str(y), scroll_speed=0.05)

        return h

def main():
    uploadData(time_stamp(), get_temperature(),  get_humidity(),  get_pressure())

if __name__ == "__main__":
    main()

