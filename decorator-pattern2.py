from abc import ABC, abstractmethod

class Coffee(ABC):
    def get_description(self):
        return "Coffee"

    @abstractmethod
    def cost(self):
        pass


class SimpleCoffee(Coffee):
    def cost(self):
        return 2.0


class CoffeeDecorator(Coffee):
    def __init__(self, decorated_coffee):
        self.decorated_coffee = decorated_coffee

    def get_description(self):
        return self.decorated_coffee.get_description()

    def cost(self):
        return self.decorated_coffee.cost()


class MilkDecorator(CoffeeDecorator):
    def get_description(self):
        return f"{self.decorated_coffee.get_description()}, Milk"

    def cost(self):
        return self.decorated_coffee.cost() + 0.5


class SugarDecorator(CoffeeDecorator):
    def get_description(self):
        return f"{self.decorated_coffee.get_description()}, Sugar"

    def cost(self):
        return self.decorated_coffee.cost() + 0.3


# TODO: Implement VanillaDecorator that adds vanilla flavor to coffee
class VanillaDecorator(CoffeeDecorator):
    def get_description(self):
        return f"{self.decorated_coffee.get_description()}, Vanilla"

    def cost(self):
        return self.decorated_coffee.cost() + 0.7


# Main function to test the decorators
my_coffee = SimpleCoffee()
print(f"Description: {my_coffee.get_description()}, Cost: {my_coffee.cost()}")

my_coffee = MilkDecorator(my_coffee)
print(f"Description: {my_coffee.get_description()}, Cost: {my_coffee.cost()}")

my_coffee = SugarDecorator(my_coffee)
print(f"Description: {my_coffee.get_description()}, Cost: {my_coffee.cost()}")

# Add VanillaDecorator similar to MilkDecorator and SugarDecorator
my_coffee = VanillaDecorator(my_coffee)
print(f"Description: {my_coffee.get_description()}, Cost: {my_coffee.cost()}")
