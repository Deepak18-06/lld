"""
The Facade Pattern is a structural design pattern that provides a simplified interface to a complex subsystem. 
It hides the complexities of the subsystem and provides a single, unified interface through which the client can 
interact with the system, making it easier for the client to use the subsystem without needing to understand its inner workings.

Key Concepts:
Facade: The class that provides the simplified interface to the complex subsystem.
Subsystem: A collection of classes or components that perform complex operations. The client interacts with these through the Facade.
Client: The class or application that uses the Facade to interact with the subsystem.
When to Use:
When you want to simplify interactions with a complex system by providing a higher-level interface.
When you need to decouple a system's internals from its clients to make the system easier to use.
When you want to reduce the dependency between clients and complex subsystems, making the system more flexible.

"""

# Subsystem classes
class DVDPlayer:
    def on(self):
        print("DVD Player on")
    
    def play(self, movie):
        print(f"Playing movie: {movie}")
    
    def off(self):
        print("DVD Player off")

class Projector:
    def on(self):
        print("Projector on")
    
    def off(self):
        print("Projector off")

class SoundSystem:
    def on(self):
        print("Sound System on")
    
    def set_volume(self, level):
        print(f"Setting volume to {level}")
    
    def off(self):
        print("Sound System off")

# Facade class
class HomeTheaterFacade:
    def __init__(self, dvd_player, projector, sound_system):
        self.dvd_player = dvd_player
        self.projector = projector
        self.sound_system = sound_system

    def watch_movie(self, movie):
        print("Get ready to watch a movie...")
        self.projector.on()
        self.sound_system.on()
        self.sound_system.set_volume(5)
        self.dvd_player.on()
        self.dvd_player.play(movie)

    def end_movie(self):
        print("Shutting down the theater...")
        self.dvd_player.off()
        self.sound_system.off()
        self.projector.off()

# Usage
if __name__ == "__main__":
    dvd_player = DVDPlayer()
    projector = Projector()
    sound_system = SoundSystem()

    home_theater = HomeTheaterFacade(dvd_player, projector, sound_system)
    home_theater.watch_movie("Inception")
    home_theater.end_movie()
