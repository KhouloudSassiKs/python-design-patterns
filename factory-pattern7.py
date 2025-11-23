from abc import ABC, abstractmethod

# Abstract Product A
class Spaceship(ABC):
    @abstractmethod
    def blast_off(self):
        pass


# Concrete Spaceships
class NASASpaceship(Spaceship):
    def blast_off(self):
        print("Blast off the NASA spaceship!")


class SpaceXSpaceship(Spaceship):
    def blast_off(self):
        print("Blast off the SpaceX spaceship!")


# Abstract Product B
class SpaceSuit(ABC):
    @abstractmethod
    def wear(self):
        pass


# Concrete Space Suits
class NASASpaceSuit(SpaceSuit):
    def wear(self):
        print("Wearing my NASA spacesuit.")


class SpaceXSpaceSuit(SpaceSuit):
    def wear(self):
        print("Wearing my SpaceX spacesuit.")


# Abstract Factory
class SpaceFactory(ABC):
    @abstractmethod
    def create_spaceship(self):
        pass

    @abstractmethod
    def create_space_suit(self):
        pass


# Concrete Factories
class NASAFactory(SpaceFactory):
    def create_spaceship(self):
        return NASASpaceship()

    def create_space_suit(self):
        return NASASpaceSuit()


class SpaceXFactory(SpaceFactory):
    def create_spaceship(self):
        return SpaceXSpaceship()

    def create_space_suit(self):
        return SpaceXSpaceSuit()


# Client
class SpaceMission:
    def __init__(self, space_factory: SpaceFactory):
        self.spaceship = space_factory.create_spaceship()
        self.space_suit = space_factory.create_space_suit()

    def prepare(self):
        self.spaceship.blast_off()
        self.space_suit.wear()


if __name__ == '__main__':
    space_factory = None
    agency_type = "SpaceX"  # Change to "NASA" or "SpaceX"

    if agency_type == "NASA":
        space_factory = NASAFactory()
    elif agency_type == "SpaceX":
        space_factory = SpaceXFactory()
    else:
        print("Unknown agency type.")

    if space_factory:
        mission = SpaceMission(space_factory)
        mission.prepare()
