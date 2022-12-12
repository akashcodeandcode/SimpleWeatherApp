import tkinter as tk
import requests
import time


def getWeather(canvas):
    city = txtEntry.get()
    api = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=06c921750b9a82d8f5d1294e1586276f"
    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp'] - 273.15)

    min_temp = int(json_data['main']['temp_min'] - 273.15)
    max_temp = int(json_data['main']['temp_max'] - 273.15)
    humidity = json_data['main']['humidity']

    sunrise = time.strftime("%H:%M:%S", time.gmtime(json_data['sys']['sunrise'] + 19800))
    sunset = time.strftime("%H:%M:%S", time.gmtime(json_data['sys']['sunset'] + 19800))

    temp_info = condition + "\n" + str(temp) + "°C"
    summary_info = "\n" + "Max Temp: " + str(max_temp) + "\n" + "Min Temp: " + str(min_temp) + "\n" + "Humidity: " + str(humidity) + "\n" + "Sunrise: " + sunrise + "\n" + "Sunset: " + sunset

    lbl1.config(text=temp_info)
    lbl2.config(text=summary_info)


canvas = tk.Tk()
canvas.geometry("600x400")
canvas.title("Weather App")

f = ("poppins", 15, "bold")
t = ("poppins", 30, "bold")

txtEntry = tk.Entry(canvas, font=t)
txtEntry.pack(pady=20)
txtEntry.focus()
txtEntry.bind('<Return>', getWeather)

lbl1 = tk.Label(canvas, font=t)
lbl1.pack()
lbl2 = tk.Label(canvas, font=f)
lbl2.pack()

canvas.mainloop()
