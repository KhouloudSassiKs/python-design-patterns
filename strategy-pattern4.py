from abc import ABC, abstractmethod

# Define the SerializationStrategy interface with an abstract method `serialize` that accepts an object
class SerializationStrategy(ABC):
    @abstractmethod
    def serialize(self, obj):
        pass

# JsonSerialization class that inherits from SerializationStrategy
# The `serialize` method returns a string "JSON representation of {obj}"
class JsonSerialization(SerializationStrategy):
    def serialize(self, obj):
        return f"JSON representation of {obj}"

# XmlSerialization class that inherits from SerializationStrategy
# The `serialize` method returns a string "XML representation of {obj}"
class XmlSerialization(SerializationStrategy):
    def serialize(self, obj):
        return f"XML representation of {obj}"

# Serializer class that uses a strategy for serialization
class Serializer:
    def set_serialization_strategy(self, strategy: SerializationStrategy):
        self.strategy = strategy
    
    def serialize(self, obj):
        if self.strategy:
            return self.strategy.serialize(obj)
        return None

if __name__ == "__main__":
    # Create a Serializer object
    serializer = Serializer()

    # Create JsonSerialization and XmlSerialization objects
    json_serializer = JsonSerialization()
    xml_serializer = XmlSerialization()

    # Sample dictionary to serialize
    sample_dict = {"name": "John", "age": 30, "city": "New York"}

    # Set the serialization strategy to JsonSerialization and serialize the data, then print it
    serializer.set_serialization_strategy(json_serializer)
    json_output = serializer.serialize(sample_dict)
    print(json_output)

    # Set the serialization strategy to XmlSerialization and serialize the data, then print it
    serializer.set_serialization_strategy(xml_serializer)
    xml_output = serializer.serialize(sample_dict)
    print(xml_output)
