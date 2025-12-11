from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


class Light:
    def on(self):
        print("Light is ON.")

    def off(self):
        print("Light is OFF.")


class LightOnCommand(Command):
    def __init__(self, light: Light):
        self.light = light

    def execute(self):
        self.light.on()


class LightOffCommand(Command):
    def __init__(self, light: Light):
        self.light = light

    def execute(self):
        self.light.off()


class RemoteControl:
    def __init__(self):
        self.commands = {}

    def set_command(self, name: str, command: Command):
        self.commands[name] = command

    def press_button(self, name: str):
        if name in self.commands:
            self.commands[name].execute()
        else:
            print(f"No command named '{name}' found.")


if __name__ == "__main__":
    light = Light()

    light_on_command = LightOnCommand(light)
    light_off_command = LightOffCommand(light)

    remote = RemoteControl()
    remote.set_command("lightOn", light_on_command)
    remote.set_command("lightOff", light_off_command)

    remote.press_button("lightOn")
    remote.press_button("lightOff")
    remote.press_button("invalidCommand")
