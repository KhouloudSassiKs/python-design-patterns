from abc import ABC, abstractmethod

class Sandwich(ABC):
    """Base component representing a sandwich."""

    def get_description(self):
        return "Basic Sandwich"

    @abstractmethod
    def cost(self):
        pass


class BasicSandwich(Sandwich):
    """Concrete component."""

    def cost(self):
        return 3.0


class SandwichDecorator(Sandwich):
    """Base decorator class."""

    def __init__(self, decorated_sandwich: Sandwich):
        self.decorated_sandwich = decorated_sandwich

    def get_description(self):
        return self.decorated_sandwich.get_description()

    def cost(self):
        return self.decorated_sandwich.cost()


class LettuceDecorator(SandwichDecorator):
    """Adds lettuce to the sandwich."""

    def get_description(self):
        return f"{self.decorated_sandwich.get_description()}, Lettuce"

    def cost(self):
        return self.decorated_sandwich.cost() + 0.5


class TomatoDecorator(SandwichDecorator):
    """Adds tomato to the sandwich."""

    def get_description(self):
        return f"{self.decorated_sandwich.get_description()}, Tomato"

    def cost(self):
        return self.decorated_sandwich.cost() + 0.7


class BaconDecorator(SandwichDecorator):
    """Adds bacon to the sandwich."""

    def get_description(self):
        return f"{self.decorated_sandwich.get_description()}, Bacon"

    def cost(self):
        return self.decorated_sandwich.cost() + 1.5


# Example usage
if __name__ == "__main__":
    sandwich = BasicSandwich()
    print(f"{sandwich.get_description()} - ${sandwich.cost():.2f}")

    sandwich = LettuceDecorator(sandwich)
    print(f"{sandwich.get_description()} - ${sandwich.cost():.2f}")

    sandwich = TomatoDecorator(sandwich)
    print(f"{sandwich.get_description()} - ${sandwich.cost():.2f}")

    sandwich = BaconDecorator(sandwich)
    print(f"{sandwich.get_description()} - ${sandwich.cost():.2f}")
