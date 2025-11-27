from abc import ABC, abstractmethod

# Abstract Component
class Component(ABC):
    @abstractmethod
    def display_details(self):
        pass

# Leaf class
class Animal(Component):
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def display_details(self):
        print(f"Animal: {self.name} ({self.species})")

# Composite class
class Zoo(Component):
    def __init__(self):
        self.components = []
    
    def add_component(self, comp):
        self.components.append(comp)
        
    def display_details(self):
        for comp in self.components:
            comp.display_details()

# Animals
leo = Animal("Leo", "Lion")
tina = Animal("Tina", "Tiger")
benny = Animal("Benny", "Bear")

# Zoo structures
main_zoo = Zoo()
big_cats_section = Zoo()

# Build structure
big_cats_section.add_component(leo)
big_cats_section.add_component(tina)

main_zoo.add_component(benny)
main_zoo.add_component(big_cats_section)

# Display Zoo info
main_zoo.display_details()
