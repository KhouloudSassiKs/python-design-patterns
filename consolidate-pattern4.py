from abc import ABC, abstractmethod


class TemperatureControlStrategy(ABC):
    """Abstract strategy for controlling temperature."""

    @abstractmethod
    def control_temperature(self, new_temp: int) -> None:
        pass


class HeatingStrategy(TemperatureControlStrategy):
    """Concrete strategy: heating."""

    def __init__(self, temp: int) -> None:
        self.temp = temp

    def control_temperature(self, new_temp: int) -> None:
        self.temp = new_temp
        print(f"Heating up to: {new_temp}°C")


class CoolingStrategy(TemperatureControlStrategy):
    """Concrete strategy: cooling."""

    def __init__(self, temp: int) -> None:
        self.temp = temp

    def control_temperature(self, new_temp: int) -> None:
        self.temp = new_temp
        print(f"Cooling down to: {new_temp}°C")


class ClimateControl:
    """Context class using a temperature control strategy."""

    def __init__(self, strategy: TemperatureControlStrategy) -> None:
        self.strategy = strategy

    def set_strategy(self, strategy: TemperatureControlStrategy) -> None:
        self.strategy = strategy

    def control_temperature(self, new_temp: int) -> None:
        self.strategy.control_temperature(new_temp)


if __name__ == "__main__":
    # Heating strategy
    heating = HeatingStrategy(25)
    climate_control = ClimateControl(heating)
    climate_control.control_temperature(22)

    # Switch to cooling strategy
    cooling = CoolingStrategy(20)
    climate_control.set_strategy(cooling)
    climate_control.control_temperature(18)
