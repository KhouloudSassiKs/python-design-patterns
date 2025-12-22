from abc import ABC, abstractmethod


class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class CreditCardStrategy(PaymentStrategy):
    def __init__(self, card_number):
        self.card_number = card_number

    def pay(self, amount):
        print(f"Paid {amount} using Credit Card: {self.card_number}")


class PayPalStrategy(PaymentStrategy):
    def __init__(self, email):
        self.email = email

    def pay(self, amount):
        print(f"Paid {amount} using PayPal: {self.email}")


class ShoppingCart:
    def __init__(self):
        self.payment_strategy = None

    def set_payment_strategy(self, payment_strategy: PaymentStrategy):
        self.payment_strategy = payment_strategy

    def checkout(self, amount):
        if self.payment_strategy:
            self.payment_strategy.pay(amount)
        else:
            print("No payment strategy set.")


if __name__ == "__main__":
    cart = ShoppingCart()

    credit_card = CreditCardStrategy("1234-5678-9876-5432")
    paypal = PayPalStrategy("user@example.com")

    cart.set_payment_strategy(credit_card)
    cart.checkout(100)

    cart.set_payment_strategy(paypal)
    cart.checkout(200)
