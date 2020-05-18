import requests
import json
import datetime
import time
import tkinter as tk

class Weather:
    def __init__(self,parent):
        self.api_key = '2d3e148162f779382b38d219e60e028e'
        self.city_name = 'Tokyo'
        self.url = f"http://api.openweathermap.org/data/2.5/weather?q={self.city_name}&appid={self.api_key}&lang=ja"

        self.label = tk.Label(parent,text="weather data")
        self.label2 = tk.Label(parent,text="updated time")
        self.label.pack()
        self.label2.pack()
        self.label.after(60000,self.change_info)
        self.label2.after(60000,self.change_info)


    def show_data(self):
        response = requests.get(self.url)
        data = json.loads(response.text)
       # print(data['weather'][0]['description'],datetime.datetime.now())
        return data
    
    def change_info(self):
        time = datetime.datetime.now()
        data = self.show_data()
        var = data['weather'][0]['description']
        time = datetime.datetime.now()
        self.label.configure(text=var)
        self.label2.configure(text=time) 
        self.label.after(60000,self.change_info)
        self.label2.after(60000,self.change_info)
        

    #def main(self):
       # after(60000,cgange_info)

if __name__ ==  "__main__":
    root = tk.Tk()
    weather = Weather(root)
    root.mainloop()
