'''
💡 Real-World Scenario
Scenario: You’re building a weather monitoring app. You want multiple modules to respond when weather data (like temperature, humidity) is updated — for instance:
•	Display in UI
•	Save to log
•	Alert user if temp is too high

'''
from abc import ABC,abstractmethod

#creating an observer interface
class Observer(ABC):
    @abstractmethod
    def update(self, temperature, humidity):
        pass
#Creating Subject
class WeatherStation:
    def __init__(self):
        self._observers= []
        self._temperature = None
        self._humidity = None
        
    def add_observer(self,observer:Observer):
        self._observers.append(observer)
        
    def remove_observer(self, observer:Observer):
        self._observers.remove(observer)
        
    def notify_observers(self):
        for observer in self._observers:
            observer.update(self._temperature,self._humidity)
            
    def set_weather_data(self,temperature, humidity):
        print(f"\n [Weather Station] Weather Updated : {temperature}°C, {humidity}%")
        self._temperature = temperature
        self._humidity = humidity
        self.notify_observers()
        
#Concrete Observers
class WeatherDisplay(Observer):
    def update(self,temperature,humidity):
        print(f"[Display] Current Temp: {temperature}°C, Humidity: {humidity}%")

class WeatherLogger(Observer):
    def update(self, temperature, humidity):
        print(f"[Logger] Logged data -> Temp: {temperature}, Humidity: {humidity}")
    
class HeatAlertSystem(Observer):
    def update(self, temperature, humidity):
        if temperature> 35:
            print("[Alert] Heat warning! Stay hydrated!")
            
#Usage - Observer Design Pattern
station =  WeatherStation()
display = WeatherDisplay()
logger = WeatherLogger()
alertsystem = HeatAlertSystem()


station.add_observer(display)
station.add_observer(logger)
station.add_observer(alertsystem)

station.set_weather_data(30,60)
station.set_weather_data(38,48)
