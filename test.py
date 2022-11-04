from time import sleep
import requests

# t = sense.get_temperature()
# p = sense.get_pressure()
# h = sense.get_humidity()

# temp = round(t, 1) - 16
# pressure = round(p, 1)
# humidity = round(h, 1)

# message = "Temperature: " + str(t) + " Pressure: " + str(p) + " Humidity: " + str(h)
# while True:
#     print("""------------------------------------
#     What would you like to see?
#     1. Temperature
#     2. Pressure
#     3. Humidity
#     4. Exit
#     """)
#     try:
#         inp = int(input('\n'))
#     except ValueError:
#         print("Please enter 1, 2 or 3\n")
#         continue
#     if inp == 1:
#         print(f"Temperature: {str(temp)}")
#         sense.show_message(str(temp), scroll_speed=0.05)
#     elif inp == 2:
#         print(f"Pressure: {str(pressure)}")
#         sense.show_message(str(pressure), scroll_speed=0.05)
#     elif inp == 3:
#         print(f"Humidity: {str(humidity)}")
#         sense.show_message(str(humidity), scroll_speed=0.05)
#     elif inp == 4:
#         break


def getSensorData():
    while True:
        try:
            res = requests.get("https://api.basecampserver.tech/sensors?node_id=457")
            return res.json()
        except requests.exceptions.Timeout:
            continue
        except requests.exceptions.HTTPError:
            exit("Something went wrong :(")

# def get_average(type, sensordata):
#     average = []

#     for x in sensordata:
#         average.append(x[type])
#     return sum(average)/len(average)
    
    
# print(get_average('pressure', getSensorData()))

# def standart_deviation(type):
#     g = []
#     for x in getSensorData():
#         g.append(x[type])
#     print(statistics.stdev(g))

# standart_deviation('temperature')

from tkinter import *
 
# create root window
root = Tk()
 
# root window title and dimension
root.title("Raspberry Pi measurements")
# Set geometry(widthxheight)
root.geometry('600x220')
 
# adding menu bar in root window
# new item in menu bar labelled as 'New'
# adding more items in the menu bar
menu = Menu(root)
item = Menu(menu)
item.add_command(label='Option')
menu.add_cascade(label='Option', menu=item)
root.config(menu=menu)
 
# adding a label to the root window

lbl = Label(root, text = "Choose one")
lbl.grid(column=0, row=0)
 
# adding Entry Field

# txt = Entry(root, width=10)
# txt.grid(column =1, row =0)
 
 
# function to display user text when
# button is clicked

# def temperature():
    

def clear_screen():
    for widget in root.winfo_children():
        widget.destroy()


def clicked():
    return None


def temperature():
    clear_screen()
    x = Label(root, text= 'Temperature in °C',
                    fg = 'grey').grid(column=0, row=0)
    max = Button(root, text = "    Max Temperature   ",
            fg = "grey").grid(column=0, row=1)
    min = Button(root, text = "    Min Temperature    ",
            fg = "grey").grid(column=0, row=2)
    average = Button(root, text = "Average Temperature",
            fg = "grey").grid(column=0, row=3)
    graph = Button(root, text = "Temperature in graph",
            fg = "grey").grid(column=0, row=4)
    back = Button(root, text = "Go back",
            fg = "grey", command=main).grid(column=0, row=5)


def hum():
    clear_screen()
    x = Label(root, text= 'Humidity in PH2O',
                    fg = 'grey').grid(column=0, row=0)
    max = Button(root, text = "   Max Humidity    ",
            fg = "grey").grid(column=0, row=1)
    min = Button(root, text = "    Min Humidity    ",
            fg = "grey").grid(column=0, row=2)
    average = Button(root, text = "Average Humidity",
            fg = "grey").grid(column=0, row=3)
    graph = Button(root, text = "Humidity in graph",
            fg = "grey").grid(column=0, row=4)
    back = Button(root, text = "Go back",
            fg = "grey", command=main).grid(column=0, row=5)

def pres():
    clear_screen()
    x = Label(root, text= 'Pressure in HpA',
                    fg = 'grey').grid(column=0, row=0)
    max = Button(root, text = "    Max Pressure   ",
            fg = "grey").grid(column=0, row=1)
    min = Button(root, text = "     Min Pressure   ",
            fg = "grey").grid(column=0, row=2)
    average = Button(root, text = "Average Pressure",
            fg = "grey").grid(column=0, row=3)
    graph = Button(root, text = "Pressure in graph",
            fg = "grey").grid(column=0, row=4)
    back = Button(root, text = "Go back",
            fg = "grey", command=main).grid(column=0, row=5)



# button widget with red color text inside and setting up the location with grid
def main():
    clear_screen()
    temp = Button(root, text = "             Temperature             " ,
                fg = "grey",
                command=temperature).grid(column=0, row=1)

    humidity = Button(root, text = "                 Humidity                " ,
                fg = 'grey',
                command=hum).grid(column=0, row=2)

    pressure = Button(root, text = "                Pressure                 " ,
                fg = 'grey', 
                command=pres).grid(column=0, row=3)
        
    all_data = Button(root, text = "            Show all data             " ,
                fg = 'grey', 
                command=clicked).grid(column=0, row=4)
    
    ssh = Button(root, text = "          Connect to SSH           " , 
                fg = 'red', 
                command=clicked).grid(column=0, row=5)

    upload = Button(root, text = "Upload data to Raspberry Pi" ,
                fg = 'red', 
                command=clicked).grid(column=0, row=6)

    exit = Button(root, text = "             Exit Program             " ,
                fg = 'grey', 
                command=root.quit).grid(column=0, row=7)

    # Execute Tkinter
    root.mainloop()

main()
