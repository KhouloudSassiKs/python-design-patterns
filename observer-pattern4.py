from abc import ABC, abstractmethod
from typing import List


class Subscriber(ABC):
    @abstractmethod
    def update(self, price: float):
        pass


class Stock:
    def __init__(self):
        self.subscribers: List[Subscriber] = []

    def add_subscriber(self, subscriber: Subscriber):
        if subscriber not in self.subscribers:
            self.subscribers.append(subscriber)

    def remove_subscriber(self, subscriber: Subscriber):
        if subscriber in self.subscribers:
            self.subscribers.remove(subscriber)

    def set_price(self, price: float):
        for subscriber in self.subscribers:
            subscriber.update(price)


class ConcreteSubscriber(Subscriber):
    def __init__(self, name: str):
        self.name = name

    def update(self, price: float):
        print(f"{self.name} received new stock price: {price}")


if __name__ == "__main__":
    stock = Stock()

    subscriber1 = ConcreteSubscriber("Subscriber 1")
    subscriber2 = ConcreteSubscriber("Subscriber 2")

    stock.add_subscriber(subscriber1)
    stock.add_subscriber(subscriber2)

    stock.set_price(150.0)

    stock.remove_subscriber(subscriber1)
    stock.set_price(155.5)
