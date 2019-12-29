import serial
import time
import json
from tkinter import Tk, Frame
from pi.src.Light import Light
from pi.src.LightButton import LightButton
from pi.src.Arduino import Arduino

with open('config/app.json') as config_file:
    lightButtons = {}
    config = json.load(config_file)
    controller = Arduino(
        serial.Serial(config['port'], 9600, timeout=5),
        time
    )

    app = Tk()
    app.title(config['app']['title'])
    app.geometry(str(config['app']['window_height']) + "x" + str(config['app']['window_width']))
    app.configure(background='black')
    frame = Frame(app)
    frame.pack()

    for l in config['lights']:
        light = Light(l['number'], 0, controller)
        lightButtons[l['number']] = LightButton(light, app)

app.mainloop()
