import requests
import os
import statistics
from datetime import datetime
from sense_hat import SenseHat
sense = SenseHat()


icons = {
    "temperature": "°C",
    "humidity": "PH2O",
    "pressure": "hPa"
}

def showMenu(type: str):
    os.system("clear")
    while True:
        inp = input("""[1] - Show max 
[2] - Show min
[3] - Show average
[4] - Show deviation
[5] - Go back
""")
        os.system("clear")

        res = ""
        if inp == "1":
            showWarning()
            res = f"max {type}: {getMax(type, sensorData)} {icons[type]}"
        elif inp == "2":
            showWarning()
            res = f"min {type}: {getMin(type, getMax(type, sensorData), sensorData)} {icons[type]}"
        elif inp == "3":
            showWarning()
            res = f"average {type}: {getAverage(type, sensorData)} {icons[type]}"
        elif inp == "4":
            showWarning()
            res = f"deviation {type}: {getDeviation(type, sensorData)} {icons[type]}"
        elif inp == "5":
            break

        if len(res) > 0:
            print(str(res))
            sense.show_message(str(res), scroll_speed=0.05)

def showWarning():
    print(f"\033[31m*The information is not precise\033[0m")

def getSensorData():
    print("loading data ...")
    while True:
        try:
            res = requests.get("https://api.basecampserver.tech/sensors?node_id=457", timeout=1)
            print("data fetched!")
            return res.json()
        except requests.exceptions.Timeout:
            continue
        except requests.exceptions.HTTPError:
            exit("Something went wrong :(")

def showAllData(sensorData: list) -> None:

    sortedListed = []
        
    print()
    print(f"    Timestamp         Temperature in {icons['temperature']}      Humidity in {icons['humidity']}     Pressure in {icons['pressure']} ")
    print("_________________________________________________________________________________________________________________________________")
    
    for x in sensorData:
        dt_obj = datetime.fromtimestamp(x["timestamp"])
        sortedListed.append(f'{dt_obj}  |   {x["temperature"]:15}  |   {x["humidity"]:15} |   {x["pressure"]:15} |')

    for y in sorted(sortedListed):
        print(y)

def getDeviation(type: str, sensorData: list) -> float:
    g = []
    for x in sensorData:
        g.append(x[type])
    return statistics.stdev(g)


def getAverage(type: str, sensordata: list) -> float:
    average = []
    for x in sensordata:
        average.append(x[type])
    return sum(average)/len(average)

def getMax(type: str, sensorData: list) -> str:
    max = 0
    for x in sensorData:
        if x[type] > max:
            max = x[type]
    return max


def getMin(type: str, max: float, sensorData: list) -> float:
    min = max
    for x in sensorData:
        if x[type] < min:
            min = x[type]
    return min


def main():

    while True:
        inp = input("""[T] - Temperature
[H] - Humidity
[P] - Pressure
[A] - Show all data
[Q] - Quit
""").upper()

        if inp == "T":
            showMenu("temperature")
        elif inp == "H":
            showMenu("humidity")
        elif inp == "P":
            showMenu("pressure")
        elif inp == "A":
            showAllData(sensorData)
        elif inp == "Q":
            exit()

if __name__ == "__main__":
    sensorData = getSensorData()
    main()
