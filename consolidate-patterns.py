from abc import ABC, abstractmethod


class Device(ABC):
    """Abstract base class representing a generic device."""

    @abstractmethod
    def operate_on(self):
        pass

    @abstractmethod
    def operate_off(self):
        pass


class Light(Device):
    """Concrete implementation of a Light device."""

    def operate_on(self):
        print("Lights On")

    def operate_off(self):
        print("Lights Off")


class Fan(Device):
    """Concrete implementation of a Fan device."""

    def operate_on(self):
        print("Fan On")

    def operate_off(self):
        print("Fan Off")

    def set_speed(self, speed):
        print(f"Fan speed is set to: {speed}")


class DeviceFactory(ABC):
    """Abstract factory class for creating devices."""

    @abstractmethod
    def create_device(self):
        pass


class LightFactory(DeviceFactory):
    """Factory for creating Light objects."""

    def create_device(self):
        return Light()


class FanFactory(DeviceFactory):
    """Factory for creating Fan objects."""

    def create_device(self):
        return Fan()


if __name__ == "__main__":
    # Create and use a Light
    light_factory = LightFactory()
    light = light_factory.create_device()
    light.operate_on()
    light.operate_off()

    # Create and use a Fan
    fan_factory = FanFactory()
    fan = fan_factory.create_device()
    fan.operate_on()
    fan.set_speed(24)
    fan.operate_off()
