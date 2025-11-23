from abc import ABC, abstractmethod

class EuropeanPlug:
    """Represents a European-style plug."""

    def connect(self):
        print("European plug connected.")


class USPlug(ABC):
    """Abstract interface for US-style plugs."""

    @abstractmethod
    def connect(self):
        pass


class Adapter(USPlug):
    """
    Adapter that allows a EuropeanPlug to be used where a USPlug is expected.
    """

    def __init__(self, euro_plug):
        self.euro_plug = euro_plug

    def connect(self):
        self.euro_plug.connect()


if __name__ == "__main__":
    euro_plug = EuropeanPlug()
    adapter = Adapter(euro_plug)
    adapter.connect()
