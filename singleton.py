class MusicPlayer:
    __instance = None

    @staticmethod
    def getInstance():
        if MusicPlayer.__instance is None:
            MusicPlayer.__instance = MusicPlayer()
        return MusicPlayer.__instance

    def play(self, song):
        # Play the given song
        print(f"Playing: {song}")


# Testing the Singleton pattern
if __name__ == "__main__":
    player1 = MusicPlayer.getInstance()
    player1.play("Song1.mp3")

    # Demonstrate singleton behavior
    player2 = MusicPlayer.getInstance()
    print(f"player1 is player2: {player1 is player2}")
