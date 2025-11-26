from abc import ABC, abstractmethod

class Exhibit(ABC):
    @abstractmethod
    def show_details(self):
        pass


class Painting(Exhibit):
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist

    def show_details(self):
        print(f"{self.title} by {self.artist}")


class Gallery(Exhibit):
    def __init__(self):
        self.items = []

    def add(self, exhibit):
        self.items.append(exhibit)

    def remove(self, exhibit):
        self.items.remove(exhibit)

    def show_details(self):
        for item in self.items:
            item.show_details()


if __name__ == "__main__":
    painting1 = Painting("Starry Night", "Vincent van Gogh")
    painting2 = Painting("Mona Lisa", "Leonardo da Vinci")

    gallery = Gallery()
    gallery.add(painting1)
    gallery.add(painting2)

    gallery.show_de_
