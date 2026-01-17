from abc import ABC, abstractmethod


class Observer(ABC):
    """Observer interface."""

    @abstractmethod
    def update(self, message: str) -> None:
        pass


class HomeOwner(Observer):
    """Concrete observer."""

    def __init__(self, name: str) -> None:
        self.name = name

    def update(self, message: str) -> None:
        print(f"New update for homeowner {self.name}: {message}")


class Subject:
    """Subject (publisher) that manages observers."""

    def __init__(self) -> None:
        self._observers: list[Observer] = []

    def attach(self, observer: Observer) -> None:
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        if observer in self._observers:
            self._observers.remove(observer)

    def notify(self, message: str) -> None:
        for observer in self._observers:
            observer.update(message)


class SecuritySystem(Subject):
    """Concrete subject."""

    def detect_intrusion(self) -> None:
        print("Intrusion detection activated!")
        self.notify("Intruder spotted!")


if __name__ == "__main__":
    security_system = SecuritySystem()

    khouloud = HomeOwner("Khouloud")
    alice = HomeOwner("Alice")

    security_system.attach(khouloud)
    security_system.attach(alice)

    security_system.detect_intrusion()
