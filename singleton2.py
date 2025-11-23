class ConfigManager:
    __instance = None

    @staticmethod
    def getInstance():
        # Ensure only one instance is created
        if ConfigManager.__instance is None:
            ConfigManager.__instance = ConfigManager()
        # Provide global access to the single instance
        return ConfigManager.__instance

    def load_config(self, config):
        print(f"Loading config: {config}")


# Testing the Singleton behavior
if __name__ == "__main__":
    config_manager = ConfigManager.getInstance()
    config_manager.load_config("config file path")

    another_config_manager = ConfigManager.getInstance()
    print(config_manager is another_config_manager)  # This should print True
