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


# Abstract Product Classes
class Account(ABC):
    @abstractmethod
    def account_type(self):
        pass


class DebitCard(ABC):
    @abstractmethod
    def card_type(self):
        pass


# Concrete Account Types
class SavingsAccount(Account):
    def account_type(self):
        return "Savings Account"


class CurrentAccount(Account):
    def account_type(self):
        return "Current Account"


# Concrete Debit Card Types
class SavingsDebitCard(DebitCard):
    def card_type(self):
        return "Savings Debit Card"


class CurrentDebitCard(DebitCard):
    def card_type(self):
        return "Current Debit Card"


# Abstract Factory
class AccountFactory(ABC):
    @abstractmethod
    def create_account(self):
        pass

    @abstractmethod
    def create_debit_card(self):
        pass


# Concrete Factories
class SavingsAccountFactory(AccountFactory):
    def create_account(self):
        return SavingsAccount()

    def create_debit_card(self):
        return SavingsDebitCard()


class CurrentAccountFactory(AccountFactory):
    def create_account(self):
        return CurrentAccount()

    def create_debit_card(self):
        return CurrentDebitCard()


# Demo
if __name__ == "__main__":
    savings_factory = SavingsAccountFactory()
    savings_account = savings_factory.create_account()
    savings_card = savings_factory.create_debit_card()

    logger = Logger.getInstance()
    logger.log(savings_account.account_type())
    logger.log(savings_card.card_type())

    current_factory = CurrentAccountFactory()
    current_account = current_factory.create_account()
    current_card = current_factory.create_debit_card()

    logger.log(current_account.account_type())
    logger.log(current_card.card_type())
