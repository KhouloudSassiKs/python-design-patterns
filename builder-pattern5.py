from abc import ABC, abstractmethod

# Product
class Robot:
    def __init__(self):
        self.material = None
        self.type = None
        self.power_source = None

    def set_material(self, material):
        self.material = material

    def set_type(self, r_type):
        self.type = r_type

    def set_power_source(self, power_source):
        self.power_source = power_source

    def show_robot(self):
        print(f"Robot material: {self.material}, type: {self.type}, power source: {self.power_source}")


# Abstract Builder
class RobotBuilder(ABC):
    @abstractmethod
    def build_material(self):
        pass

    @abstractmethod
    def build_type(self):
        pass

    @abstractmethod
    def build_power_source(self):
        pass

    @abstractmethod
    def get_robot(self):
        pass


# Concrete Builder
class SteelRobotBuilder(RobotBuilder):
    def __init__(self):
        self.robot = Robot()

    def build_material(self):
        self.robot.set_material("Steel")

    def build_type(self):
        self.robot.set_type("Warrior")

    def build_power_source(self):
        self.robot.set_power_source("Nuclear")

    def get_robot(self):
        return self.robot


# Director
class RobotDirector:
    def __init__(self):
        self.builder = None

    def set_builder(self, builder: RobotBuilder):
        self.builder = builder

    def construct_robot(self):
        self.builder.build_material()
        self.builder.build_type()
        self.builder.build_power_source()
        return self.builder.get_robot()


# Client
if __name__ == "__main__":
    director = RobotDirector()
    builder = SteelRobotBuilder()
    director.set_builder(builder)

    robot = director.construct_robot()
    robot.show_robot()
