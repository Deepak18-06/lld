from abc import ABC, abstractmethod


class MediaPlayer(ABC):
    @abstractmethod
    def play(self, audio_type: str, file_name: str):
        pass

class AdvanceMediaPlayer(ABC):
    @abstractmethod
    def playVlc(self, file_name: str):
        pass
    @abstractmethod
    def playMp4(self, file_name: str):
        pass

class VlcPlayer(AdvanceMediaPlayer):
    def playVlc(self, file_name: str):
        print("Playing in vlc file name ", file_name)
        
    def playMp4(self, file_name: str):
        pass

class Mp4Player(AdvanceMediaPlayer):
    def playMp4(self, file_name: str):
        print("Playing in mp4 file name ", file_name)

    def playVlc(self, file_name: str):
        pass

class MediaAdapter(MediaPlayer):
    def __init__(self, audio_type):
        if audio_type == 'vlc':
            self.advancedMediaPlayer = VlcPlayer()
        elif audio_type == 'mp4':
            self.advancedMediaPlayer = Mp4Player()
    
    def play(self, audio_type: str, file_name: str):
        if audio_type == 'vlc':
            self.advancedMediaPlayer.playVlc(file_name)
        elif audio_type == 'mp4':
            self.advancedMediaPlayer.playMp4(file_name)
    

class AudioPlayer(MediaPlayer):
    def __init__(self):
        self.media_adapter = None
    def play(self, audio_type, file_name):
        if audio_type == "mp3":
            print("Playing mp3 file", file_name)
        elif audio_type == 'vlc' or audio_type == "mp4":
            self.media_adapter = MediaAdapter(audio_type)
            self.media_adapter.play(audio_type, file_name)
        else:
            print("Invalid media format")
    


if __name__ == "__main__":
    audioPlayer = AudioPlayer()

    audioPlayer.play("mp3", "shaka_laka.mp3")
    audioPlayer.play('vlc', "home_alone.mp4")