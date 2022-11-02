import requests
import time
import random
import json


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

def main():
    while True:
        uploadData(time.time(), random.randint(3, 12),  random.randint(3, 12),  random.randint(3, 13))
        time.sleep(10)



if __name__ == "__main__":
    main()

