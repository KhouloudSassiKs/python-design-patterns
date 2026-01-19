from abc import ABC, abstractmethod


class Light:
    """Basic Light class."""

    def turn_on(self):
        print("Lights are On")

    def turn_off(self):
        print("Lights are Off")


class LightDecorator(ABC):
    """Abstract decorator for Light."""

    @abstractmethod
    def operate(self, cmd: str):
        pass


class ColorChangeDecorator(LightDecorator):
    """Decorator that adds color-change behavior."""

    def __init__(self, light: Light):
        self.light = light

    def operate(self, cmd: str):
        print("with colors")
        if cmd == "on":
            self.light.turn_on()
        elif cmd == "off":
            self.light.turn_off()
        else:
            print("Unknown operation")


def main():
    light = Light()
    light.turn_on()
    light.turn_off()

    colored_light = ColorChangeDecorator(light)
    colored_light.operate("on")
    colored_light.operate("off")


if __name__ == "__main__":
    main()
