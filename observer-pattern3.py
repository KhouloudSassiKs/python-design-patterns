from abc import ABC, abstractmethod
from typing import List


class Follower(ABC):
    @abstractmethod
    def update(self, post: str):
        pass


class Blog:
    def __init__(self):
        self.followers: List[Follower] = []

    def add_follower(self, follower: Follower):
        if follower not in self.followers:
            self.followers.append(follower)

    def new_post(self, post: str):
        for follower in self.followers:
            follower.update(post)


class ConcreteFollower(Follower):
    def __init__(self, name: str):
        self.name = name

    def update(self, post: str):
        print(f"{self.name} received new blog post: {post}")


if __name__ == "__main__":
    blog = Blog()

    follower1 = ConcreteFollower("Follower 1")
    follower2 = ConcreteFollower("Follower 2")

    blog.add_follower(follower1)
    blog.add_follower(follower2)

    blog.new_post("How to use Observer Pattern")
    blog.new_post("Advanced Python Tips")
