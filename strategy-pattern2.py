from abc import ABC, abstractmethod


class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount: float) -> None:
        """Process a payment of the given amount."""
        pass


class CreditCardStrategy(PaymentStrategy):
    def __init__(self, card_number: str) -> None:
        self.card_number = card_number

    def pay(self, amount: float) -> None:
        print(f"Paid {amount} using Credit Card: {self.card_number}")


class PayPalStrategy(PaymentStrategy):
    def __init__(self, email: str) -> None:
        self.email = email

    def pay(self, amount: float) -> None:
        print(f"Paid {amount} using PayPal: {self.email}")


class BitcoinStrategy(PaymentStrategy):
    def __init__(self, wallet_address: str) -> None:
        self.wallet_address = wallet_address

    def pay(self, amount: float) -> None:
        print(f"Paid {amount} using Bitcoin: {self.wallet_address}")


class ShoppingCart:
    def __init__(self) -> None:
        self.strategy: PaymentStrategy | None = None

    def set_payment_strategy(self, payment: PaymentStrategy) -> None:
        self.strategy = payment

    def checkout(self, amount: float) -> None:
        if not self.strategy:
            print("No payment strategy set.")
            return
        self.strategy.pay(amount)


if __name__ == "__main__":
    payment_strategies = [
        CreditCardStrategy("1234-5678-9876-5432"),
        PayPalStrategy("user@example.com"),
        BitcoinStrategy("1A2b3C4d5E6f7G8h9I0j1K2L3m4N5o6P7")
    ]

    shopping_cart = ShoppingCart()

    for strategy in payment_strategies:
        shopping_cart.set_payment_strategy(strategy)
        shopping_cart.checkout(100)
