from abc import ABC, abstractmethod

# Abstract Products
class Button(ABC):
    @abstractmethod
    def paint(self):
        pass


class Checkbox(ABC):
    @abstractmethod
    def paint(self):
        pass


# Concrete Products - Windows
class WinButton(Button):
    def paint(self):
        print("Rendering a button in a Windows style.")


class WinCheckbox(Checkbox):
    def paint(self):
        print("Rendering a checkbox in a Windows style.")


# Concrete Products - Mac
class MacButton(Button):
    def paint(self):
        print("Rendering a button in a Mac style.")


class MacCheckbox(Checkbox):
    def paint(self):
        print("Rendering a checkbox in a Mac style.")


# Concrete Products - Linux
class LinuxButton(Button):
    def paint(self):
        print("Rendering a button in a Linux style.")


class LinuxCheckbox(Checkbox):
    def paint(self):
        print("Rendering a checkbox in a Linux style.")


# Abstract Factory
class GUIFactory(ABC):
    @abstractmethod
    def create_button(self):
        pass

    @abstractmethod
    def create_checkbox(self):
        pass


# Concrete Factories
class WinFactory(GUIFactory):
    def create_button(self):
        return WinButton()

    def create_checkbox(self):
        return WinCheckbox()


class MacFactory(GUIFactory):
    def create_button(self):
        return MacButton()

    def create_checkbox(self):
        return MacCheckbox()


class LinuxFactory(GUIFactory):
    def create_button(self):
        return LinuxButton()

    def create_checkbox(self):
        return LinuxCheckbox()


# Client Code
class Application:
    def __init__(self, factory: GUIFactory):
        self.button = factory.create_button()
        self.checkbox = factory.create_checkbox()

    def paint(self):
        self.button.paint()
        self.checkbox.paint()


if __name__ == '__main__':
    os_type = "Linux"   # Change to "Mac" or "Windows" for testing

    if os_type == "Windows":
        factory = WinFactory()
    elif os_type == "Mac":
        factory = MacFactory()
    elif os_type == "Linux":
        factory = LinuxFactory()
    else:
        factory = None
        print("Unknown OS type.")

    if factory:
        app = Application(factory)
        app.paint()
