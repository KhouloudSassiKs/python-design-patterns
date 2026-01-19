from abc import ABC, abstractmethod


class Notification(ABC):
    """Abstract base class for notifications."""

    @abstractmethod
    def send(self) -> None:
        pass


class TextNotification(Notification):
    """Concrete text notification."""

    def __init__(self, text: str) -> None:
        self.text = text

    def send(self) -> None:
        print(f"Text notification sent: {self.text}")


class EmailNotification(Notification):
    """Concrete email notification."""

    def __init__(self, email: str) -> None:
        self.email = email

    def send(self) -> None:
        print(f"Email notification sent: {self.email}")


class NotificationPool:
    """Composite class managing multiple notifications."""

    def __init__(self) -> None:
        self.notifs: list[Notification] = []

    def add_notif(self, notification: Notification) -> None:
        self.notifs.append(notification)

    def remove_notif(self, notification: Notification) -> None:
        if notification in self.notifs:
            self.notifs.remove(notification)

    def notify_the_pool(self) -> None:
        for notif in self.notifs:
            notif.send()


def main():
    text1 = TextNotification("Hello texting you")
    text2 = TextNotification("Texting again")
    email1 = EmailNotification("Hello emailing you")
    email2 = EmailNotification("Emailing again")

    notification_pool = NotificationPool()
    notification_pool.add_notif(text1)
    notification_pool.add_notif(text2)
    notification_pool.add_notif(email1)
    notification_pool.add_notif(email2)

    # Notify all
    notification_pool.notify_the_pool()

    # Remove some
    notification_pool.remove_notif(text1)
    notification_pool.remove_notif(email1)

    # Notify remaining
    notification_pool.notify_the_pool()


if __name__ == "__main__":
    main()
