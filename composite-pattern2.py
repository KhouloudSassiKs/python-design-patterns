from abc import ABC, abstractmethod

class Musician(ABC):
    @abstractmethod
    def show_details(self):
        pass


class SoloArtist(Musician):
    def __init__(self, name, instrument):
        self.name = name
        self.instrument = instrument

    def show_details(self):
        print(f"{self.name} plays the {self.instrument}.")


# Band composite class
class Band(Musician):
    def __init__(self):
        self.members = []

    def add(self, musician):
        self.members.append(musician)

    def show_details(self):
        for musician in self.members:
            musician.show_details()


# Test the classes
if __name__ == "__main__":
    artist1 = SoloArtist("John Doe", "guitar")
    artist2 = SoloArtist("Jane Smith", "keyboard")

    band = Band()
    band.add(artist1)
    band.add(artist2)

    band.show_details()
