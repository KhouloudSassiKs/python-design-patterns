from abc import ABC, abstractmethod


class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount: float) -> None:
        """Process a payment of the given amount."""
        raise NotImplementedError


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


class AmazonPayStrategy(PaymentStrategy):
    def __init__(self, email: str) -> None:
        self.email = email

    def pay(self, amount: float) -> None:
        print(f"Paid {amount} using Amazon Pay: {self.email}")


class ShoppingCart:
    def __init__(self) -> None:
        self.strategy: PaymentStrategy | None = None

    def set_payment_strategy(self, strategy: PaymentStrategy) -> None:
        self.strategy = strategy

    def checkout(self, amount: float) -> None:
        if not self.strategy:
            raise RuntimeError("No payment strategy set.")
        self.strategy.pay(amount)


if __name__ == "__main__":
    cart = ShoppingCart()

    credit_card = CreditCardStrategy("1234-5678-9876-5432")
    paypal = PayPalStrategy("user@example.com")
    amazon = AmazonPayStrategy("amazon@user.com")

    cart.set_payment_strategy(credit_card)
    cart.checkout(100)

    cart.set_payment_strategy(paypal)
    cart.checkout(150)

    cart.set_payment_strategy(amazon)
    cart.checkout(200)
