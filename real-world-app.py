from abc import ABC, abstractmethod


class User:
    def __init__(self, name: str):
        self.name = name

    def receive_message(self, message: str) -> None:
        print(f"{self.name} received message: {message}")


# Abstract Command class
class Command(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass


# ChatRoom class
class ChatRoom:
    def __init__(self):
        self.users: list[User] = []

    def show_message(self, message: str) -> None:
        print(f"Message broadcasted: {message}")

    def add_user(self, user: User) -> None:
        self.users.append(user)

    def send_message(self, message: str) -> None:
        for user in self.users:
            user.receive_message(message)


# Concrete Command implementation
class ChatCommand(Command):
    def __init__(self, chat_room: ChatRoom, message: str):
        self.chat_room = chat_room
        self.message = message

    def execute(self) -> None:
        self.chat_room.show_message(self.message)
        self.chat_room.send_message(self.message)


if __name__ == "__main__":
    chat_room = ChatRoom()

    user1 = User("Alice")
    user2 = User("Bob")

    chat_room.add_user(user1)
    chat_room.add_user(user2)

    chat_command = ChatCommand(chat_room, "Hello, everyone!")
    chat_command.execute()
