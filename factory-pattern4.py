from abc import ABC, abstractmethod

# Abstract Products
class Controller(ABC):
    @abstractmethod
    def connect(self):
        pass


class Headset(ABC):
    @abstractmethod
    def connect(self):
        pass


# Concrete Products - PlayStation
class PlayStationController(Controller):
    def connect(self):
        print("Connecting PlayStation controller.")


class PlayStationHeadset(Headset):
    def connect(self):
        print("Connecting PlayStation headset.")


# Concrete Products - Xbox
class XboxController(Controller):
    def connect(self):
        print("Connecting Xbox controller.")


class XboxHeadset(Headset):
    def connect(self):
        print("Connecting Xbox headset.")


# Abstract Factory
class AccessoryFactory(ABC):
    @abstractmethod
    def create_controller(self):
        pass

    @abstractmethod
    def create_headset(self):
        pass


# Concrete Factories
class PlayStationFactory(AccessoryFactory):
    def create_controller(self):
        return PlayStationController()

    def create_headset(self):
        return PlayStationHeadset()


class XboxFactory(AccessoryFactory):
    def create_controller(self):
        return XboxController()

    def create_headset(self):
        return XboxHeadset()


# Client Code
class GameSetup:
    def __init__(self, factory: AccessoryFactory):
        self.controller = factory.create_controller()
        self.headset = factory.create_headset()

    def setup(self):
        self.controller.connect()
        self.headset.connect()


if __name__ == '__main__':
    system_type = "Xbox"  # Change to "PlayStation" to test PS setup

    if system_type == "PlayStation":
        factory = PlayStationFactory()
    elif system_type == "Xbox":
        factory = XboxFactory()
    else:
        factory = None
        print("Unknown system type.")

    if factory:
        setup = GameSetup(factory)
        setup.setup()
