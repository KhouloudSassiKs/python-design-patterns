from abc import ABC, abstractmethod

class LegacySoundSystem:
    """A legacy sound system with an old interface."""
    
    def play_sound(self):
        print("Sound playing from legacy system.")


class ModernSoundSystemInterface(ABC):
    """Modern interface that new systems are expected to implement."""
    
    @abstractmethod
    def output_sound(self):
        pass


class SoundSystemAdapter(ModernSoundSystemInterface):
    """Adapter that wraps a legacy system so it can be used like a modern one."""
    
    def __init__(self, system):
        self.system = system

    def output_sound(self):
        self.system.play_sound()


# Usage example
if __name__ == "__main__":
    legacy_system = LegacySoundSystem()
    adapter = SoundSystemAdapter(legacy_system)

    adapter.output_sound()
