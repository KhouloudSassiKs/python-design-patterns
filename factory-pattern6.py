from abc import ABC, abstractmethod

# Abstract Product A
class MainCourse(ABC):
    @abstractmethod
    def serve(self):
        pass


# Abstract Product B
class Drink(ABC):
    @abstractmethod
    def pour(self):
        pass


# Concrete Main Courses
class Pasta(MainCourse):
    def serve(self):
        print("Serving Pasta")


class Steak(MainCourse):
    def serve(self):
        print("Serving Steak")


# Concrete Drinks
class Wine(Drink):
    def pour(self):
        print("Pouring Wine")


class Juice(Drink):
    def pour(self):
        print("Pouring
