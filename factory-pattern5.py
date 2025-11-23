from abc import ABC, abstractmethod

# Abstract Product A
class Slider(ABC):
    @abstractmethod
    def render(self):
        pass


# Concrete Product A1
class WinSlider(Slider):
    def render(self):
        print("Rendering a slider in a Windows style.")


# Concrete Product A2
class MacSlider(Slider):
    def render(self):
        print("Rendering a slider in a Mac style.")


# Abstract Product B
class Toggle(ABC):
    @abstractmethod
    def render(self):
        pass


# Concrete Product B1
class WinToggle(Toggle):
    def render(self):
        print("Rendering a toggle in a Windows style.")


# Concrete Product B2
class MacToggle(Toggle):
    def render(self):
        print("Rendering a toggle in a Mac style.")


# Abstract Factory
class UIComponentFactory(ABC):
    @abstractmethod
    def create_slider(self):
        pass

    @abstractmethod
    def create_toggle(self):
        pass


# Concrete Factory 1
class WinUIFactory(UIComponentFactory):
    def create_slider(self):
        return WinSlider()

    def create_toggle(self):
        return WinToggle()


# Concrete Factory 2
class MacUIFactory(UIComponentFactory):
    def create_slider(self):
        return MacSlider()

    def create_toggle(self):
        return MacToggle()


# Client
class MobileApplication:
    def __init__(self, factory: UIComponentFactory):
        self.__factory = factory
        self.__slider = factory.create_slider()
        self.__toggle = factory.create_toggle()

    def render(self):
        self.__slider.render()
        self.__toggle.render()


if __name__ == '__main__':
    os_type = "Mac"  # Change to "Windows" or "Mac"

    if os_type == "Windows":
        factory = WinUIFactory()
    elif os_type == "Mac":
        factory = MacUIFactory()
    else:
        factory = None
        print("Unknown OS type.")

    if factory:
        mobile_app = MobileApplication(factory)
        mobile_app.render()
