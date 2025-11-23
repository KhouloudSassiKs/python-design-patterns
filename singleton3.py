class Logger:
    __instance = None

    @staticmethod
    def getInstance():
        # Ensure only one instance of Logger exists
        if Logger.__instance is None:
            Logger.__instance = Logger()
        return Logger.__instance

    def log(self, message):
        # Print the log message
        print(message)


if __name__ == "__main__":
    # Create an instance of Logger using getInstance and call the log method
    logger = Logger.getInstance()
    logger.log("Server started")
