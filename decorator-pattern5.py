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


# TODO: Implement the CoffeeDecorator class that inherits from Coffee
class CoffeeDecorator(Coffee):
    # Implement the constructor to initialize the decorated_coffee member variable
    def __init__(self, decorated_coffee):
        self.decorated_coffee = decorated_coffee

    # Implement the get_description method to return the decorated coffee's description
    def get_description(self):
        return self.decorated_coffee.get_description()

    # Implement the cost method to return the decorated coffee's cost
    def cost(self):
        return self.decorated_coffee.cost()


# TODO: Define CinnamonDecorator class to add cinnamon flavor to coffee with a cost of 0.3 dollars
class CinnamonDecorator(CoffeeDecorator):
    # Implement the get_description method
    def get_description(self):
        return f"{self.decorated_coffee.get_description()}, Cinnamon"

    # Implement the cost method
    def cost(self):
        return self.decorated_coffee.cost() + 0.3


if __name__ == "__main__":
    my_coffee = SimpleCoffee()
    print(f"Description: {my_coffee.get_description()}, Cost: {my_coffee.cost()}")

    # TODO: Update my_coffee to use CinnamonDecorator
    my_coffee = CinnamonDecorator(my_coffee)
    print(f"Description: {my_coffee.get_description()}, Cost: {my_coffee.cost()}")
