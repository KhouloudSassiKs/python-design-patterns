from abc import ABC, abstractmethod
from typing import List


class Observer(ABC):
    @abstractmethod
    def update(self, temperature: float):
        pass


class WeatherStation:
    def __init__(self):
        self.observers: List[Observer] = []

    def add_observer(self, observer: Observer):
        if observer not in self.observers:
            self.observers.append(observer)

    def remove_observer(self, observer: Observer):
        if observer in self.observers:
            self.observers.remove(observer)

    def set_temperature(self, temperature: float):
        for observer in self.observers:
            observer.update(temperature)


class ConcreteObserver(Observer):
    def __init__(self, name: str):
        self.name = name

    def update(self, temperature: float):
        print(f"{self.name} received temperature update: {temperature}°C")


if __name__ == "__main__":
    weather_station = WeatherStation()

    observer1 = ConcreteObserver("Observer 1")
    observer2 = ConcreteObserver("Observer 2")

    weather_station.add_observer(observer1)
    weather_station.add_observer(observer2)

    weather_station.set_temperature(25)

    weather_station.remove_observer(observer1)
    weather_station.set_temperature(30)
