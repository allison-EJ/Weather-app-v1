import time
from tkinter import *
import tkinter as tk
import requests


def getweather(root):
    city = textfield.get()
    api = f"https://api.openweathermap.org/data/2.5/weather?q=" + city +"&appid=4632117b6b689b06ff17b78aa889073c"
    json_data = requests.get(api).json()
    condition = json_data["weather"][0]["main"]
    temp = int(json_data["main"]["temp"] -273.15)
    min_temp = int(json_data["main"]["temp_min"] - 273.15)
    max_temp = int(json_data["main"]["temp_max"] - 273.15)
    pressure = json_data["main"]["pressure"]
    humidity = json_data["main"]["humidity"]
    wind = json_data["wind"]["speed"]
    sunrise = time.strftime("%H:%M", time.gmtime(json_data["sys"]["sunrise"] + 3600))
    sunset = time.strftime("%H:%M", time.gmtime(json_data["sys"]["sunset"] + 3600))

    final_info = condition + "\n" + str(temp) + "°C"
    final_data = "\n" + "Max Temp: " + str(max_temp) + "\n" + "Min Temp: " + str(min_temp) + "\n" + "Pressure: " + str(pressure) + "\n" + "Humidity: " + str(humidity) + "\n" + "Wind Speed: " + str(wind) + "\n" + "Sunrise: " + str(sunrise) + "\n" + "Sunset: " + str(sunset)
    label1.config(text=final_info)
    label2.config(text=final_data)


root = Tk()
root.title("World Weather App")
root.geometry("900x500+300+200")
root.resizable(False, False)


f = ("poppins", 15, "bold")
t = ("poppins", 30, "bold")

textfield = tk.Entry(root, justify="center", font=t)
textfield.pack(pady=20)
textfield.focus()
textfield.bind("<Return>", getweather)

label1 = tk.Label(root, font=t)
label1.pack()

label2 = tk.Label(root, font=f)
label2.pack()

root.mainloop()