from abc import ABC, abstractmethod


class User:
    """Observer that receives messages from the chat room."""

    def __init__(self, name: str):
        self.name = name

    def receive_message(self, message: str) -> None:
        print(f"{self.name} received the message: {message}")


class Command(ABC):
    """Abstract Command interface."""

    @abstractmethod
    def execute(self) -> None:
        pass


class ChatRoom:
    """Manages users and broadcasts messages."""

    def __init__(self):
        self.users: list[User] = []

    def show_message(self, message: str) -> None:
        print(f"Message broadcasted: {message}")

    def add_user(self, user: User) -> None:
        self.users.append(user)

    def send_message(self, message: str) -> None:
        for user in self.users:
            user.receive_message(message)


class ChatCommand(Command):
    """Concrete command to send a message to the chat room."""

    def __init__(self, chat_room: ChatRoom, message: str):
        self.chat_room = chat_room
        self.message = message

    def execute(self) -> None:
        self.chat_room.show_message(self.message)
        self.chat_room.send_message(self.message)


def main() -> None:
    chat_room = ChatRoom()

    alice = User("Alice")
    bob = User("Bob")

    chat_room.add_user(alice)
    chat_room.add_user(bob)

    chat_command = ChatCommand(chat_room, "Hello, everyone!")
    chat_command.execute()


if __name__ == "__main__":
    main()
