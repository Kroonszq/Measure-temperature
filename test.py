from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

temp = round(sense.get_temperature(),2)

while True:
    print(temp)

    sense.show_message(str(temp))