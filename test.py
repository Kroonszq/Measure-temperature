from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

t = sense.get_temperature()
p = sense.get_pressure()
h = sense.get_humidity()

temp = round(t, 1) - 16
pressure = round(p, 1)
humidity = round(h, 1)

message = "Temperature: " + str(t) + " Pressure: " + str(p) + " Humidity: " + str(h)
while True:
    print("""------------------------------------
    What would you like to see?
    1. Temperature
    2. Pressure
    3. Humidity
    4. Exit
    """)
    try:
        inp = int(input('\n'))
    except ValueError:
        print("Please enter 1, 2 or 3\n")
        continue
    if inp == 1:
        print(f"Temperature: {str(temp)}")
        sense.show_message(str(temp), scroll_speed=0.05)
    elif inp == 2:
        print(f"Pressure: {str(pressure)}")
        sense.show_message(str(pressure), scroll_speed=0.05)
    elif inp == 3:
        print(f"Humidity: {str(humidity)}")
        sense.show_message(str(humidity), scroll_speed=0.05)
    elif inp == 4:
        break

