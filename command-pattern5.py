from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


class Radio:
    def on(self):
        print("Turning Radio ON")

    def off(self):
        print("Turning Radio OFF")

    def volume_high(self):
        print("Setting Radio volume to HIGH")


class TV:
    def on(self):
        print("Turning TV ON")

    def off(self):
        print("Turning TV OFF")

    def set_channel(self):
        print("Setting TV channel")


class RadioOnCommand(Command):
    def __init__(self, radio: Radio):
        self.radio = radio

    def execute(self):
        self.radio.on()


class RadioOffCommand(Command):
    def __init__(self, radio: Radio):
        self.radio = radio

    def execute(self):
        self.radio.off()


class RadioVolumeHighCommand(Command):
    def __init__(self, radio: Radio):
        self.radio = radio

    def execute(self):
        self.radio.volume_high()


class TVOnCommand(Command):
    def __init__(self, tv: TV):
        self.tv = tv

    def execute(self):
        self.tv.on()


class TVOffCommand(Command):
    def __init__(self, tv: TV):
        self.tv = tv

    def execute(self):
        self.tv.off()


class TVSetChannelCommand(Command):
    def __init__(self, tv: TV):
        self.tv = tv

    def execute(self):
        self.tv.set_channel()


class RemoteControl:
    def __init__(self):
        self.command: Command | None = None

    def set_command(self, command: Command):
        self.command = command

    def execute(self):
        if self.command:
            self.command.execute()


if __name__ == "__main__":
    radio = Radio()
    tv = TV()

    radio_on = RadioOnCommand(radio)
    radio_off = RadioOffCommand(radio)
    radio_volume_high = RadioVolumeHighCommand(radio)

    tv_on = TVOnCommand(tv)
    tv_off = TVOffCommand(tv)
    tv_set_channel = TVSetChannelCommand(tv)

    remote = RemoteControl()

    remote.set_command(radio_on)
    remote.execute()

    remote.set_command(radio_volume_high)
    remote.execute()

    remote.set_command(radio_off)
    remote.execute()

    remote.set_command(tv_on)
    remote.execute()

    remote.set_command(tv_set_channel)
    remote.execute()

    remote.set_command(tv_off)
    remote.execute()
