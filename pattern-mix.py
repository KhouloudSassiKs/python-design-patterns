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


# Abstract Loan class
class Loan(ABC):
    @abstractmethod
    def display(self):
        pass


# Concrete Loan Types
class HomeLoan(Loan):
    def display(self):
        Logger.getInstance().log("Home Loan created.")


class CarLoan(Loan):
    def display(self):
        Logger.getInstance().log("Car Loan created.")


# Abstract Factory
class LoanFactory(ABC):
    @abstractmethod
    def create_loan(self):
        pass


# Concrete Factories
class HomeLoanFactory(LoanFactory):
    def create_loan(self):
        return HomeLoan()


class CarLoanFactory(LoanFactory):
    def create_loan(self):
        return CarLoan()


# Demo usage
if __name__ == "__main__":
    home_loan_factory = HomeLoanFactory()
    home_loan = home_loan_factory.create_loan()
    home_loan.display()

    car_loan_factory = CarLoanFactory()
    car_loan = car_loan_factory.create_loan()
    car_loan.display()
