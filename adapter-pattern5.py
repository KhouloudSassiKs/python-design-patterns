from abc import ABC, abstractmethod

# Vintage car class with legacy behavior
class VintageCar:
    def drive(self):
        print("Driving a vintage car.")


# Modern car interface
class ModernCarInterface(ABC):
    @abstractmethod
    def start(self):
        pass


# Adapter that makes a VintageCar compatible with ModernCarInterface
class CarAdapter(ModernCarInterface):
    def __init__(self, car: VintageCar):
        self.car = car

    def start(self):
        self.car.drive()


if __name__ == "__main__":
    vintage_car = VintageCar()
    car_adapter = CarAdapter(vintage_car)
    car_adapter.start()
