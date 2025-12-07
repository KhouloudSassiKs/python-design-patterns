from abc import ABC, abstractmethod

# ============================
# Messaging Platform Interface
# ============================

class MessagingPlatform(ABC):
    @abstractmethod
    def send_message(self):
        pass


# ============================
# Concrete Messaging Platforms
# ============================

class WhatsApp(MessagingPlatform):
    def send_message(self):
        print("WhatsApp message")


class Telegram(MessagingPlatform):
    def send_message(self):
        print("Telegram message")


class Slack(MessagingPlatform):
    def send_message(self):
        print("Slack message")


# ============================
# Adapter Implementations
# ============================

class WhatsAppAdapter(MessagingPlatform):
    def __init__(self, platform):
        self.platform = platform

    def send_message(self):
        self.platform.send_message()


class TelegramAdapter(MessagingPlatform):
    def __init__(self, platform):
        self.platform = platform

    def send_message(self):
        self.platform.send_message()


class SlackAdapter(MessagingPlatform):
    def __init__(self, platform):
        self.platform = platform

    def send_message(self):
        self.platform.send_message()


# ============================
# Message Component Interface
# ============================

class MessageComponent(ABC):
    @abstractmethod
    def show_details(self):
        pass


# ============================
# Concrete Messages
# ============================

class TextMessage(MessageComponent):
    def __init__(self, content, path):
        self.content = content
        self.path = path

    def show_details(self):
        print(f"Message content: {self.content} | Path: {self.path}")


class ImageMessage(MessageComponent):
    def __init__(self, content, path):
        self.content = content
        self.path = path

    def show_details(self):
        print(f"Message content: {self.content} | Path: {self.path}")


# ============================
# Composite: Message Group
# ============================

class MessageGroup(MessageComponent):
    def __init__(self):
        self.components = []

    def add(self, comp):
        self.components.append(comp)

    def remove(self, comp):
        self.components.remove(comp)

    def show_details(self):
        for comp in self.components:
            comp.show_details()


# ============================
# Decorators
# ============================

class MessageDecorator(MessageComponent):
    def __init__(self, comp):
        self.comp = comp

    def show_details(self):
        self.comp.show_details()


class ReadReceiptDecorator(MessageDecorator):
    def show_details(self):
        self.comp.show_details()
        print("✔ Read receipt")


class TimestampDecorator(MessageDecorator):
    def show_details(self):
        self.comp.show_details()
        print("⏱ Timestamp added")


# ============================
# Main Function
# ============================

if __name__ == "__main__":

    # Messaging platform adapters
    whatsapp_adapter = WhatsAppAdapter(WhatsApp())
    telegram_adapter = TelegramAdapter(Telegram())
    slack_adapter = SlackAdapter(Slack())

    whatsapp_adapter.send_message()
    telegram_adapter.send_message()
    slack_adapter.send_message()

    # Messages and decorators
    text_message = TextMessage("Hello, I am texting!", "text_folder/")
    image_message = ImageMessage("Hello, I am sending an image!", "image_folder/")

    text_with_receipt = ReadReceiptDecorator(text_message)
    image_with_timestamp = TimestampDecorator(image_message)

    # Message group (Composite)
    group = MessageGroup()
    group.add(text_with_receipt)
    group.add(image_with_timestamp)
    group.add(text_message)
    group.add(image_message)

    group.show_details()
