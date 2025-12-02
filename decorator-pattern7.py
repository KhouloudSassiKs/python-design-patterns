from abc import ABC, abstractmethod

# Base Weapon class
class Weapon(ABC):
    @abstractmethod
    def power(self):
        pass

    def get_description(self):
        return "My weapon"

# Concrete Sword class
class Sword(Weapon):
    def power(self):
        return 20.0

    def get_description(self):
        return "Sword"

# Base decorator class
class WeaponDecorator(Weapon):
    def __init__(self, decorated_weapon: Weapon):
        self.decorated_weapon = decorated_weapon

    def get_description(self):
        return self.decorated_weapon.get_description()

# Fire power decorator
class FirePowerDecorator(WeaponDecorator):
    def get_description(self):
        return f"{self.decorated_weapon.get_description()} with Fire Power"

    def power(self):
        return self.decorated_weapon.power() + 10.0

# Ice power decorator
class IcePowerDecorator(WeaponDecorator):
    def get_description(self):
        return f"{self.decorated_weapon.get_description()} with Ice Power"

    def power(self):
        return self.decorated_weapon.power() + 8.0

# Example usage
if __name__ == "__main__":
    # Base sword
    my_sword = Sword()
    print(f"Using {my_sword.get_description()}, Power: {my_sword.power()}")

    # Add fire power
    my_sword = FirePowerDecorator(my_sword)
    print(f"Using {my_sword.get_description()}, Power: {my_sword.power()}")

    # Add ice power
    my_sword = IcePowerDecorator(my_sword)
    print(f"Using {my_sword.get_description()}, Power: {my_sword.power()}")
