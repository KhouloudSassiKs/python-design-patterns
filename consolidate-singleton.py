class SmartKeyManager:
    __instance = None

    @staticmethod
    def get_instance():
        if SmartKeyManager.__instance is None:
            SmartKeyManager.__instance = SmartKeyManager()
        return SmartKeyManager.__instance

    def unlock_door(self):
        print("Door unlocked")

    def lock_door(self):
        print("Door locked")


if __name__ == "__main__":
    key_manager1 = SmartKeyManager.get_instance()
    key_manager1.unlock_door()

    key_manager2 = SmartKeyManager.get_instance()
    key_manager2.lock_door()

    print(key_manager1 is key_manager2)  # Outputs: True
