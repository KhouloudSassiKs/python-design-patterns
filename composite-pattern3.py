from abc import ABC, abstractmethod

class Task(ABC):
    @abstractmethod
    def show_info(self):
        pass


class SimpleTask(Task):
    def __init__(self, description, duration):
        self.description = description
        self.duration = duration

    def show_info(self):
        print(f"{self.description} will take {self.duration} hours.")


class Project(Task):
    def __init__(self):
        self.tasks = []

    def add(self, task):
        self.tasks.append(task)

    def show_info(self):
        for task in self.tasks:
            task.show_info()


if __name__ == "__main__":
    task1 = SimpleTask("Design", 5)
    task2 = SimpleTask("Implementation", 10)

    project = Project()
    project.add(task1)
    project.add(task2)

    project.show_info()
