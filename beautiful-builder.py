class SmartHomeDevice:
    def __init__(self):
        self.sensors = []
        self.actuators = []

    def set_sensors(self, sensor):
        self.sensors.append(sensor)

    def set_actuators(self, actuator):
        self.actuators.append(actuator)

    def show_details(self):
        sensors = "', '".join(self.sensors)
        actuators = "', '".join(self.actuators)
        print(f"SmartHomeDevice Sensors: ['{sensors}'], Actuators: ['{actuators}']")


class SmartHomeDeviceBuilder:
    def __init__(self):
        self.device = SmartHomeDevice()

    def add_sensors(self, sensor):
        self.device.set_sensors(sensor)
        return self

    def add_actuators(self, actuator):
        self.device.set_actuators(actuator)
        return self

    def build(self):
        return self.device


if __name__ == "__main__":
    light_sensor = "Light Sensor"
    temperature_sensor = "Temperature Sensor"
    led = "LED"
    heater = "Heater"

    builder = SmartHomeDeviceBuilder()
    home_device = (
        builder.add_sensors(light_sensor)
               .add_sensors(temperature_sensor)
               .add_actuators(led)
               .add_actuators(heater)
               .build()
    )

    home_device.show_details()
