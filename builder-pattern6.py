from abc import ABC, abstractmethod

# Product
class House:
    def __init__(self):
        self.foundation = None
        self.structure = None
        self.roof = None

    def set_foundation(self, foundation):
        self.foundation = foundation

    def set_structure(self, structure):
        self.structure = structure

    def set_roof(self, roof):
        self.roof = roof

    def show_house(self):
        print(f"House with {self.foundation}, {self.structure}, and {self.roof}.")


# Abstract Builder
class HouseBuilder(ABC):
    @abstractmethod
    def build_foundation(self):
        pass

    @abstractmethod
    def build_structure(self):
        pass

    @abstractmethod
    def build_roof(self):
        pass

    @abstractmethod
    def get_house(self):
        pass


# Concrete Builder
class ConcreteHouseBuilder(HouseBuilder):
    def __init__(self):
        self.house = House()

    def build_foundation(self):
        self.house.set_foundation("Concrete Foundation")

    def build_structure(self):
        self.house.set_structure("Concrete Structure")

    def build_roof(self):
        self.house.set_roof("Concrete Roof")

    def get_house(self):
        return self.house


# Director
class Director:
    def __init__(self):
        self.builder = None

    def set_builder(self, builder: HouseBuilder):
        self.builder = builder

    def construct_house(self):
        self.builder.build_foundation()
        self.builder.build_structure()
        self.builder.build_roof()
        return self.builder.get_house()


# Client
if __name__ == "__main__":
    director = Director()
    builder = ConcreteHouseBuilder()
    director.set_builder(builder)

    house = director.construct_house()
    house.show_house()
