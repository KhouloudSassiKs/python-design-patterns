from abc import ABC, abstractmethod


class Employee(ABC):
    @abstractmethod
    def show_details(self):
        pass


class Developer(Employee):
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def show_details(self):
        print(f"{self.name} works as {self.position}.")


class Manager(Employee):
    def __init__(self):
        self.employees = []

    def add(self, employee: Employee):
        self.employees.append(employee)

    def remove(self, employee: Employee):
        self.employees.remove(employee)

    def show_details(self):
        for employee in self.employees:
            employee.show_details()


if __name__ == "__main__":
    dev1 = Developer("John Doe", "Senior Developer")
    dev2 = Developer("Jane Smith", "Junior Developer")

    manager = Manager()
    manager.add(dev1)
    manager.add(dev2)

    manager.show_details()
