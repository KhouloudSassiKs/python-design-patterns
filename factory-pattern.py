from abc import ABC, abstractmethod

# Abstract Product
class Transport(ABC):
    @abstractmethod
    def drive(self):
        """Define how the transport operates."""
        pass


# Concrete Products
class Car(Transport):
    def drive(self):
        return "Driving a car"


class Bike(Transport):
    def drive(self):
        return "Riding a bike"


# Abstract Creator
class TransportFactory(ABC):
    @abstractmethod
    def create_vehicle(self):
        """Factory method for creating a transport."""
        pass


# Concrete Creators
class CarFactory(TransportFactory):
    def create_vehicle(self):
        return Car()


class BikeFactory(TransportFactory):
    def create_vehicle(self):
        return Bike()


# Client Code
def main():
    factories = [CarFactory(), BikeFactory()]

    for factory in factories:
        vehicle = factory.create_vehicle()
        print(vehicle.drive())


if __name__ == "__main__":
    main()
