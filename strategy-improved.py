from abc import ABC, abstractmethod


# =========================
# Message Format Strategies
# =========================

class MessageFormatStrategy(ABC):
    """Strategy interface for message formatting."""

    @abstractmethod
    def format_message(self, message: str) -> str:
        pass


class UppercaseMessageFormat(MessageFormatStrategy):
    """Formats messages to uppercase."""

    def format_message(self, message: str) -> str:
        return message.upper()


class LowercaseMessageFormat(MessageFormatStrategy):
    """Formats messages to lowercase."""

    def format_message(self, message: str) -> str:
        return message.lower()


# ==========
# Chat Model
# ==========

class User:
    def __init__(self, name: str):
        self.name = name

    def receive_message(self, message: str) -> None:
        print(f"{self.name} received message: {message}")


class ChatRoom:
    def __init__(self):
        self.users = []

    def add_user(self, user: User) -> None:
        self.users.append(user)

    def send_message(self, message: str) -> None:
        for user in self.users:
            user.receive_message(message)


# ==========
# Commands
# ==========

class Command(ABC):
    """Command interface."""

    @abstractmethod
    def execute(self) -> None:
        pass


class ChatCommand(Command):
    """Command that formats and sends a message to a chat room."""

    def __init__(
        self,
        room: ChatRoom,
        formatter: MessageFormatStrategy,
        message: str,
    ):
        self.room = room
        self.formatter = formatter
        self.message = message

    def execute(self) -> None:
        formatted_message = self.formatter.format_message(self.message)
        self.room.send_message(formatted_message)


# ==========
# Entry Point
# ==========

def main() -> None:
    user1 = User("Alice")
    user2 = User("Bob")

    chat_room = ChatRoom()
    chat_room.add_user(user1)
    chat_room.add_user(user2)

    upper = UppercaseMessageFormat()
    lower = LowercaseMessageFormat()

    ChatCommand(chat_room, upper, "to upper").execute()
    ChatCommand(chat_room, lower, "TO LOWER").execute()


if __name__ == "__main__":
    main()
