from abc import ABC, abstractmethod
from typing import List


class Subscriber(ABC):
    @abstractmethod
    def update(self, article: str):
        pass


class BlogPublisher:
    def __init__(self):
        self.subscribers: List[Subscriber] = []

    def add_subscriber(self, subscriber: Subscriber):
        if subscriber not in self.subscribers:
            self.subscribers.append(subscriber)

    def remove_subscriber(self, subscriber: Subscriber):
        if subscriber in self.subscribers:
            self.subscribers.remove(subscriber)

    def publish(self, article: str):
        for subscriber in self.subscribers:
            subscriber.update(article)


class ConcreteSubscriber(Subscriber):
    def __init__(self, name: str):
        self.name = name

    def update(self, article: str):
        print(f"{self.name} received a new article: {article}")


def main():
    blog_publisher = BlogPublisher()

    subscriber1 = ConcreteSubscriber("Subscriber 1")
    subscriber2 = ConcreteSubscriber("Subscriber 2")

    blog_publisher.add_subscriber(subscriber1)
    blog_publisher.add_subscriber(subscriber2)

    blog_publisher.publish("New Article 1")

    blog_publisher.remove_subscriber(subscriber1)
    blog_publisher.publish("New Article 2")


if __name__ == "__main__":
    main()
