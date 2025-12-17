from abc import ABC, abstractmethod
from typing import List


class Device(ABC):
    @abstractmethod
    def update(self, weather: str):
        pass


class WeatherStation:
    def __init__(self):
        self.devices: List[Device] = []

    def add_device(self, device: Device):
        if device not in self.devices:
            self.devices.append(device)

    def remove_device(self, device: Device):
        if device in self.devices:
            self.devices.remove(device)

    def set_weather(self, weather: str):
        for device in self.devices:
            device.update(weather)


class ConcreteDevice(Device):
    def __init__(self, name: str):
        self.name = name

    def update(self, weather: str):
        print(f"{self.name} is displaying: {weather}")


if __name__ == "__main__":
    station = WeatherStation()

    device1 = ConcreteDevice("Device 1")
    device2 = ConcreteDevice("Device 2")

    station.add_device(device1)
    station.add_device(device2)

    station.set_weather("Sunny")

    station.remove_device(device1)
    station.set_weather("Rainy")
