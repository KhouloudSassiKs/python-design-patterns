from abc import ABC, abstractmethod

# ============================
# Command Interface
# ============================

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


# ============================
# Receiver: Fan
# ============================

class Fan:
    def on(self):
        print("Fan is on.")

    def off(self):
        print("Fan is off.")


# ============================
# Concrete Commands
# ============================

class FanOnCommand(Command):
    def __init__(self, fan):
        self.fan = fan

    def execute(self):
        self.fan.on()


class FanOffCommand(Command):
    def __init__(self, fan):
        self.fan = fan

    def execute(self):
        self.fan.off()


# ============================
# Invoker: Remote Control
# ============================

class RemoteControl:
    def __init__(self):
        self.command = None

    def set_command(self, command):
        self.command = command

    def press_button(self):
        if self.command:
            self.command.execute()


# ============================
# Main
# ============================

if __name__ == "__main__":
    fan = Fan()
    fan_on = FanOnCommand(fan)
    fan_off = FanOffCommand(fan)

    remote = RemoteControl()

    remote.set_command(fan_on)
    remote.press_button()

    remote.set_command(fan_off)
    remote.press_button()
