from abc import ABC, abstractmethod

# ============================================
# Payment Gateway Interface
# ============================================
class PaymentGateway(ABC):
    @abstractmethod
    def process_payment(self):
        pass


# ============================================
# Payment Implementations
# ============================================
class PayPal(PaymentGateway):
    def process_payment(self):
        print("Paying with PayPal!")


class Stripe(PaymentGateway):
    def process_payment(self):
        print("Paying with Stripe!")


class Square(PaymentGateway):
    def process_payment(self):
        print("Paying with Square!")


# ============================================
# Adapters (your inheritance preserved)
# ============================================
class PayPalAdapter(PayPal):
    def __init__(self, paypal):
        self.paypal = paypal

    def process_payment(self):
        self.paypal.process_payment()


class StripeAdapter(Stripe):
    def __init__(self, stripe):
        self.stripe = stripe

    def process_payment(self):
        self.stripe.process_payment()


class SquareAdapter(Square):
    def __init__(self, square):
        self.square = square

    def process_payment(self):
        self.square.process_payment()


# ============================================
# Composite Pattern: Product Components
# ============================================
class ProductComponent(ABC):
    @abstractmethod
    def show_details(self):
        pass


class Product(ProductComponent):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def show_details(self):
        print(f"The component '{self.name}' costs: {self.price}")


class ProductBundle(ProductComponent):
    def __init__(self):
        self.components = []

    def add(self, component):
        self.components.append(component)

    def remove(self, component):
        self.components.remove(component)

    def show_details(self):
        for component in self.components:
            component.show_details()


# ============================================
# Decorator Pattern (NO super calls)
# ============================================
class ProductFeature(ProductComponent):
    def __init__(self, product_component):
        self.product_component = product_component

    def show_details(self):
        self.product_component.show_details()


class DiscountFeature(ProductFeature):
    def add_discount(self):
        print(" + Discount feature")

    def show_details(self):
        # No super call
        self.product_component.show_details()
        self.add_discount()


class GiftWrapFeature(ProductFeature):
    def add_gift_wrap(self):
        print(" + Gift wrap feature")

    def show_details(self):
        # No super call
        self.product_component.show_details()
        self.add_gift_wrap()


# ============================================
# Main
# ============================================
if __name__ == "__main__":
    # Payment adapter usage
    paypal = PayPal()
    stripe = Stripe()
    square = Square()

    paypal_adapter = PayPalAdapter(paypal)
    stripe_adapter = StripeAdapter(stripe)
    square_adapter = SquareAdapter(square)

    paypal_adapter.process_payment()
    stripe_adapter.process_payment()
    square_adapter.process_payment()

    # Products with decorators
    product1 = Product("Orange", "2 EUR per kilo")
    product2 = Product("Apples", "1 EUR per kilo")

    product1 = DiscountFeature(product1)
    product2 = GiftWrapFeature(product2)

    # Bundle
    grocery_bundle = ProductBundle()
    grocery_bundle.add(product1)
    grocery_bundle.add(product2)

    grocery_bundle.show_details()
