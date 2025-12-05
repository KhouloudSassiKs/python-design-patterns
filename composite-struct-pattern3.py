from abc import ABC, abstractmethod

# Base Coffee class
class Coffee(ABC):
    @abstractmethod
    def get_description(self):
        pass
        
    @abstractmethod
    def cost(self):
        pass


# Simple Coffee
class SimpleCoffee(Coffee):
    def get_description(self):
        return "Simple coffee"
    
    def cost(self):
        return 10


# Decorator base class
class CoffeeDecorator(Coffee):
    def __init__(self, coffee):
        self.coffee = coffee
    
    def get_description(self):
        return self.coffee.get_description()
    
    def cost(self):
        return self.coffee.cost()


# Vanilla Decorator
class VanillaDecorator(CoffeeDecorator):
    def get_description(self):
        return self.coffee.get_description() + " with Vanilla"
    
    def cost(self):
        return self.coffee.cost() + 5  # add-on cost


# Milk Decorator
class MilkDecorator(CoffeeDecorator):
    def get_description(self):
        return self.coffee.get_description() + " with Milk"
    
    def cost(self):
        return self.coffee.cost() + 7  # add-on cost


# Coffee Set (Composite pattern)
class CoffeeSet(Coffee):
    def __init__(self):
        self.coffees = []
    
    def add(self, coffee):
        self.coffees.append(coffee)

    def get_description(self):
        descriptions = [coffee.get_description() for coffee in self.coffees]
        return "\n".join(descriptions)
            
    def cost(self):
        return sum(coffee.cost() for coffee in self.coffees)


if __name__ == "__main__":
    # Create coffees
    simple1 = SimpleCoffee()
    simple2 = SimpleCoffee()

    vanilla = VanillaDecorator(simple1)
    milk = MilkDecorator(simple2)

    coffees = CoffeeSet()
    coffees.add(vanilla)
    coffees.add(milk)

    print(coffees.get_description())
    print(f"Total cost: {coffees.cost()}")
