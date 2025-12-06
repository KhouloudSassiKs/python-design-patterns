from abc import ABC, abstractmethod

# Base image class
class BaseImage(ABC):
    @abstractmethod
    def display(self):
        pass


# Windows image
class WinImage(BaseImage):
    def display(self):
        print("Windows Image")


# Mac image
class MacImage(BaseImage):
    def display(self):
        print("Mac Image")


# Adapter: Makes a Windows image behave like a Mac image
class WinToMacAdapter(MacImage):
    def __init__(self):
        self.win_image = WinImage()

    def display(self):
        self.win_image.display()


# Image gallery (Composite pattern)
class ImageGallery(BaseImage):
    def __init__(self):
        self.images = []

    def add(self, image):
        self.images.append(image)

    def remove(self, image):
        self.images.remove(image)

    def display(self):
        for image in self.images:
            image.display()


if __name__ == "__main__":
    winimage = WinImage()
    macimage = MacImage()
    wintomac = WinToMacAdapter()

    imageGallery = ImageGallery()
    imageGallery.add(macimage)
    imageGallery.add(wintomac)

    imageGallery.display()
