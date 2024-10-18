"""
The Command Pattern is a behavioral design pattern that turns a request into a stand-alone object containing all 
the information about the request, such as what the request is, who made the request, and what should be done. 
This encapsulation allows for delayed execution of the request, queuing, logging, and undoable operations.

Key Concepts:
Command Interface: Declares an interface for executing operations (e.g., execute()).
Concrete Command: Implements the command interface and binds together a receiver object and an action.
Receiver: The object that knows how to perform the specific action.
Invoker: Calls the command to execute the request.
Client: Creates the concrete command and assigns it to an invoker.
When to Use:
When you need to parameterize objects with operations.
When you need to queue, log, or support undo operations.
When you want to decouple the invoker (request sender) from the receiver (request handler)
"""

# Command Interface
class Command:
    def execute(self):
        pass

# Receiver Class
class Light:
    def turn_on(self):
        print("The light is on")

    def turn_off(self):
        print("The light is off")

# Concrete Command for turning on the light
class TurnOnLightCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_on()

# Concrete Command for turning off the light
class TurnOffLightCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_off()

# Invoker Class
class RemoteControl:
    def __init__(self):
        self.command = None

    def set_command(self, command):
        self.command = command

    def press_button(self):
        self.command.execute()

# Usage
if __name__ == "__main__":
    light = Light()

    # Create command objects
    turn_on = TurnOnLightCommand(light)
    turn_off = TurnOffLightCommand(light)

    # Set up the invoker (remote control)
    remote = RemoteControl()

    # Turn on the light
    remote.set_command(turn_on)
    remote.press_button()

    # Turn off the light
    remote.set_command(turn_off)
    remote.press_button()
