from abc import ABC, abstractmethod

class Car(ABC):
    @abstractmethod
    def drive(self):
        pass

class Sedan(Car):
    def drive(self):
        print("Driving a sedan.")

class SUV(Car):
    def drive(self):
        print("Driving an SUV.")

class CarFactory(ABC):
    @abstractmethod
    def create_car(self):
        pass

class SedanFactory(CarFactory):
    def create_car(self):
        return Sedan()

class SUVFactory(CarFactory):
    def create_car(self):
        return SUV()

# Create a car using the given factory and drive it
def create_and_drive_cars(factory):
    car = factory.create_car()
    car.drive()

if __name__ == "__main__":
    # Create and drive both types of cars
    sedan_factory = SedanFactory()
    create_and_drive_cars(sedan_factory)

    suv_factory = SUVFactory()
    create_and_drive_cars(suv_factory)
