from abc import ABC, abstractmethod


# Singleton Logger
class Logger:
    __instance = None

    @staticmethod
    def getInstance():
        if Logger.__instance is None:
            Logger.__instance = Logger()
        return Logger.__instance

    def log(self, message):
        print(message)


# Abstract Customer Class
class Customer(ABC):
    @abstractmethod
    def show_info(self):
        pass


# Premium Customer
class PremiumCustomer(Customer):
    def __init__(self):
        self.name = None
        self.id = None
        self.email = None

    def set_name(self, name):
        self.name = name

    def set_id(self, idc):
        self.id = idc

    def set_email(self, email):
        self.email = email

    def show_info(self):
        Logger.getInstance().log(
            f"Premium Customer: {self.name} with ID: {self.id} and Email: {self.email}"
        )


# Regular Customer
class RegularCustomer(Customer):
    def __init__(self):
        self.name = None
        self.id = None
        self.email = None

    def set_name(self, name):
        self.name = name

    def set_id(self, idc):
        self.id = idc

    def set_email(self, email):
        self.email = email

    def show_info(self):
        Logger.getInstance().log(
            f"Regular Customer: {self.name} with ID: {self.id} and Email: {self.email}"
        )


# Abstract Builder
class CustomerBuilder(ABC):
    @abstractmethod
    def build_name(self, name):
        pass

    @abstractmethod
    def build_id(self, idc):
        pass

    @abstractmethod
    def build_email(self, email):
        pass

    @abstractmethod
    def get_customer(self):
        pass


# Premium Customer Builder
class PremiumCustomerBuilder(CustomerBuilder):
    def __init__(self):
        self.customer = PremiumCustomer()

    def build_name(self, name):
        self.customer.set_name(name)

    def build_id(self, idc):
        self.customer.set_id(idc)

    def build_email(self, email):
        self.customer.set_email(email)

    def get_customer(self):
        return self.customer


# Regular Customer Builder
class RegularCustomerBuilder(CustomerBuilder):
    def __init__(self):
        self.customer = RegularCustomer()

    def build_name(self, name):
        self.customer.set_name(name)

    def build_id(self, idc):
        self.customer.set_id(idc)

    def build_email(self, email):
        self.customer.set_email(email)

    def get_customer(self):
        return self.customer


# Director
class CustomerDirector:
    def __init__(self):
        self.builder = None

    def set_builder(self, builder):
        self.builder = builder

    def construct_customer(self, name, idc, email):
        self.builder.build_name(name)
        self.builder.build_id(idc)
        self.builder.build_email(email)
        return self.builder.get_customer()


# Example Usage
if __name__ == "__main__":
    direc
