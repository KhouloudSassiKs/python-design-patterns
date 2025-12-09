from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


class MusicPlayer:
    def play(self):
        print("Music Player is playing.")

    def stop(self):
        print("Music Player is stopped.")


class PlayMusicCommand(Command):
    def __init__(self, player: MusicPlayer):
        self.player = player

    def execute(self):
        self.player.play()


class StopMusicCommand(Command):
    def __init__(self, player: MusicPlayer):
        self.player = player

    def execute(self):
        self.player.stop()


class RemoteControl:
    def __init__(self):
        self.command: Command | None = None

    def set_command(self, command: Command):
        self.command = command

    def press_button(self):
        if self.command:
            self.command.execute()


if __name__ == "__main__":
    player = MusicPlayer()
    play_music = PlayMusicCommand(player)
    stop_music = StopMusicCommand(player)

    remote = RemoteControl()
    remote.set_command(play_music)
    remote.press_button()
    remote.set_command(stop_music)
    remote.press_button()
