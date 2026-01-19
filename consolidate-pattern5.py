from abc import ABC, abstractmethod


class Device(ABC):
    @abstractmethod
    def turn_on(self) -> None:
        pass

    @abstractmethod
    def turn_off(self) -> None:
        pass


class Light(Device):
    def turn_on(self) -> None:
        print("Turning On the Lights")

    def turn_off(self) -> None:
        print("Turning Off the Lights")


class Fan(Device):
    def turn_on(self) -> None:
        print("Turning On the Fan")

    def turn_off(self) -> None:
        print("Turning Off the Fan")


class DeviceFactory(ABC):
    @abstractmethod
    def create_device(self) -> Device:
        pass


class LightFactory(DeviceFactory):
    def create_device(self) -> Device:
        return Light()


class FanFactory(DeviceFactory):
    def create_device(self) -> Device:
        return Fan()


class Command(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass


class TurnOnCommand(Command):
    def __init__(self, device: Device) -> None:
        self.device = device

    def execute(self) -> None:
        self.device.turn_on()


class TurnOffCommand(Command):
    def __init__(self, device: Device) -> None:
        self.device = device

    def execute(self) -> None:
        self.device.turn_off()


class RemoteControl:
    def __init__(self) -> None:
        self.cmd: Command | None = None

    def set_command(self, cmd: Command) -> None:
        self.cmd = cmd

    def execute(self) -> None:
        if self.cmd:
            self.cmd.execute()


def main() -> None:
    light_factory = LightFactory()
    fan_factory = FanFactory()

    light = light_factory.create_device()
    fan = fan_factory.create_device()

    light_on = TurnOnCommand(light)
    light_off = TurnOffCommand(light)
    fan_on = TurnOnCommand(fan)
    fan_off = TurnOffCommand(fan)

    remote = RemoteControl()

    remote.set_command(light_on)
    remote.execute()

    remote.set_command(light_off)
    remote.execute()

    remote.set_command(fan_on)
    remote.execute()

    remote.set_command(fan_off)
    remote.execute()


if __name__ == "__main__":
    main()
