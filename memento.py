'''
The Memento Pattern is a behavioral design pattern that allows an object to 
capture its internal state so that it can be restored to that state later.
This pattern is useful when you need to provide undo functionality or maintain the 
history of changes in an object's state.

- Memento represents the snapshot of the originator's internal state.
- Originator is the object whose state needs to be saved and restored.
- Caretaker keeps track of multiple mementos and can retrieve them.
'''
class Memento:
    def __init__(self, state):
        self._state = state

    def get_state(self):
        return self._state


class Originator:
    def __init__(self):
        self._state = ""

    def set_state(self, state):
        print(f"Setting state to: {state}")
        self._state = state

    def create_memento(self):
        print("Creating memento...")
        return Memento(self._state)

    def restore_memento(self, memento):
        print("Restoring state from memento...")
        self._state = memento.get_state()

    def show_state(self):
        print(f"Current state: {self._state}")


class Caretaker:
    def __init__(self):
        self._mementos = []

    def add_memento(self, memento):
        print("Saving memento...")
        self._mementos.append(memento)

    def get_memento(self, index):
        print("Retrieving memento...")
        return self._mementos[index]


if __name__ == "__main__":
    originator = Originator()
    caretaker = Caretaker()

    originator.set_state("State 1")
    caretaker.add_memento(originator.create_memento())

    originator.set_state("State 2")
    caretaker.add_memento(originator.create_memento())

    originator.show_state()

    originator.restore_memento(caretaker.get_memento(0))
    originator.show_state()

    originator.restore_memento(caretaker.get_memento(1))
    originator.show_state()
