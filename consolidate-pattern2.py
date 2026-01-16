# Base device class
class Device:
    """Base class for all devices."""
    def operate(self):
        pass


class Light(Device):
    """Concrete Light implementation."""
    def operate(self):
        print("Operate the lights")


class Fan(Device):
    """Concrete Fan implementation."""
    def operate(self):
        print("Operate the fan")


# Simple factory class
class DeviceFactory:
    """Factory to create device instances."""

    @staticmethod
    def create_device(device_type: str) -> Device:
        device_type = device_type.lower()

        if device_type == "light":
            return Light()
        elif device_type == "fan":
            return Fan()

        raise ValueError(f"Unknown device type: {device_type}")


# EU plug adapter interface
class EUPlugInterface:
    """Interface for devices compatible with EU sockets."""
    def plug_into_eu_socket(self):
        pass


class DeviceAdapter(EUPlugInterface):
    """Adapter that allows a Device to be used with the EU plug interface."""

    def __init__(self, device: Device):
        self.device = device

    def plug_into_eu_socket(self):
        self.device.operate()


# Example usage
if __name__ == "__main__":
    factory = DeviceFactory()

    # Light
    light = factory.create_device("light")
    light_adapter = DeviceAdapter(light)
    light_adapter.plug_into_eu_socket()

    # Fan
    fan = factory.create_device("fan")
    fan_adapter = DeviceAdapter(fan)
    fan_adapter.plug_into_eu_socket()
