"""
The Template Method Pattern is a behavioral design pattern that defines the skeleton of an algorithm in a base class (or superclass) 
and allows subclasses to override specific steps of the algorithm without changing its overall structure. The idea is to let 
subclasses modify parts of the algorithm while keeping the structure and sequence of operations consistent.

Key Concepts:
Abstract Class (Template): Defines the skeleton of the algorithm and includes the steps as methods, some of which may be abstract 
or have default implementations.
Concrete Class: Implements or overrides the methods that vary to provide specific behavior for those steps.
When to Use:
When you have an algorithm where the overall structure is the same, but some steps may vary.
When you want to enforce a common algorithm structure across multiple subclasses while allowing flexibility in certain steps.
When code duplication needs to be minimized across multiple classes that share a common structure.
"""

from abc import ABC, abstractmethod

# Abstract Class (Template)
class Game(ABC):
    # Template method
    def play(self):
        self.start()
        self.play_game()
        self.end()

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def play_game(self):
        pass

    @abstractmethod
    def end(self):
        pass

# Concrete Class 1
class Football(Game):
    def start(self):
        print("Football Game Started")

    def play_game(self):
        print("Playing Football Game")

    def end(self):
        print("Football Game Ended")

# Concrete Class 2
class Chess(Game):
    def start(self):
        print("Chess Game Started")

    def play_game(self):
        print("Playing Chess Game")

    def end(self):
        print("Chess Game Ended")

# Usage
if __name__ == "__main__":
    football = Football()
    football.play()

    print()

    chess = Chess()
    chess.play()
