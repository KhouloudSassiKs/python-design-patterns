from abc import ABC, abstractmethod

# Product
class Robot:
    def __init__(self):
        self.head = None
        self.body = None
        self.legs = None

    def set_head(self, head):
        self.head = head

    def set_body(self, body):
        self.body = body

    def set_legs(self, legs):
        self.legs = legs

    def show_robot(self):
        print(f"Robot with {self.head}, {self.body}, and {self.legs}.")


# Abstract Builder
class RobotBuilder(ABC):
    @abstractmethod
    def build_head(self):
        pass

    @abstractmethod
    def build_body(self):
        pass

    @abstractmethod
    def build_legs(self):
        pass

    @abstractmethod
    def get_robot(self):
        pass


# Concrete Builder
class MetalRobotBuilder(RobotBuilder):
    def __init__(self):
        self.robot = Robot()

    def build_head(self):
        self.robot.set_head("Metallic Head")

    def build_body(self):
        self.robot.set_body("Metallic Body")

    def build_legs(self):
        self.robot.set_legs("Metallic Legs")

    def get_robot(self):
        return self.robot


# Director
class Computer:
    def __init__(self):
        self.builder = None

    def set_builder(self, builder: RobotBuilder):
        self.builder = builder

    def construct_robot(self):
        self.builder.build_head()
        self.builder.build_body()
        self.builder.build_legs()
        return self.builder.get_robot()


# Client
if __name__ == "__main__":
    computer = Computer()
    builder = MetalRobotBuilder()
    computer.set_builder(builder)
    robot = computer.construct_robot()
    robot.show_robot()
