from abc import ABC, abstractmethod

# Adaptees
class EuropeanPlug:
    def connect(self):
        print("European plug connected.")

class BritishPlug:
    def connect(self):
        print("British plug connected.")


# Target Interface
class USPlug(ABC):
    @abstractmethod
    def connect(self):
        pass


# Adapter
class Adapter(USPlug):
    def __init__(self, plug):
        self.plug = plug

    def connect(self):
        self.plug.connect()


# Client
if __name__ == "__main__":
    european_plug = EuropeanPlug()
    british_plug = BritishPlug()

    # Example: adapting a British plug to USPlug
    adapter = Adapter(british_plug)
    adapter.connect()  # Output: British plug connected.
