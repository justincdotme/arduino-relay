import serial
import time
import json
import tkinter as tk
from pi.src.light import Light
from pi.src.arduino import Arduino

with open('config/app.json') as config_file:
    data = json.load(config_file)

    baud = 9600
    timeout = 5
    s = serial.Serial(data['port'], baud, timeout=5)
    controller = Arduino(s, time)

    lights = {}

    winHeight = 400
    winWidth = 400

    container = tk.Tk()
    frame = tk.Frame(container)
    frame.pack()

    for l in data['lights']:
        lightNum = l['number']

        lights[lightNum] = Light(lightNum, 0, controller)

        btnOnText = str(lightNum) + " On"
        btnOffText = str(lightNum) + " Off"

        button = tk.Button(
            frame,
            text=btnOnText,
            fg="green",
            command=lambda lightNum=lightNum: lights[lightNum].set_state(1)
        )
        button.pack(side=tk.LEFT)

        button = tk.Button(
            frame,
            text=btnOffText,
            fg="red",
            command=lambda lightNum=lightNum: lights[lightNum].set_state(0)
        )
        button.pack(side=tk.LEFT)


container.mainloop()
