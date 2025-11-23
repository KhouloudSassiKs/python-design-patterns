from abc import ABC, abstractmethod

class BritishPlug:
    """Represents a British-style plug."""

    def engage(self):
        print("British plug engaged.")


class USPlug(ABC):
    """Abstract interface for US-style plugs."""

    @abstractmethod
    def connect(self):
        pass


class BritishToUSAdapter(USPlug):
    """Adapter allowing a BritishPlug to be used where a USPlug is required."""

    def __init__(self, plug):
        self.plug = plug

    def connect(self):
        self.plug.engage()


# Testing the adapter pattern
if __name__ == "__main__":
    british_plug = BritishPlug()
    adapter = BritishToUSAdapter(british_plug)
    adapter.connect()
