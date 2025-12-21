from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

class TV:
    def on(self):
        print("Turning the TV ON")

    def off(self):
        print("Turning the TV OFF")


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


class RemoteControl:
    def __init__(self):
        self.command: Command | None = None

    def set_command(self, command: Command):
        self.command = command

    def press_button(self):
        if self.command:
            self.command.execute()


if __name__ == "__main__":
    tv = TV()
    tv_on_command = TVOnCommand(tv)
    tv_off_command = TVOffCommand(tv)

    remote = RemoteControl()
    remote.set_command(tv_on_command)
    remote.press_button()
    remote.set_command(tv_off_command)
    remote.press_button()
