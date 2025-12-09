from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


class Radio:
    def on(self):
        print("Radio is on.")

    def off(self):
        print("Radio is off.")

    def set_frequency(self, frequency: float):
        print(f"Radio frequency set to {frequency}.")


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


class RadioSetFrequencyCommand(Command):
    def __init__(self, radio: Radio, frequency: float):
        self.radio = radio
        self.frequency = frequency

    def execute(self):
        self.radio.set_frequency(self.frequency)


class RemoteControl:
    def __init__(self):
        self.command: Command | None = None

    def set_command(self, command: Command):
        self.command = command

    def press_button(self):
        if self.command:
            self.command.execute()


if __name__ == "__main__":
    radio = Radio()
    radio_on_command = RadioOnCommand(radio)
    radio_off_command = RadioOffCommand(radio)
    set_frequency_command = RadioSetFrequencyCommand(radio, 101.1)

    remote = RemoteControl()
    remote.set_command(radio_on_command)
    remote.press_button()
    remote.set_command(set_frequency_command)
    remote.press_button()
    remote.set_command(radio_off_command)
    remote.press_button()
