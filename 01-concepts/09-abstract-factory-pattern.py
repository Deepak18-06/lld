"""
The Abstract Factory Pattern is a creational design pattern that provides an interface for creating families of 
related or dependent objects without specifying their concrete classes. It’s an extension of the Factory Method Pattern, 
where instead of creating a single product, the Abstract Factory creates a family of related objects (products).

This pattern is especially useful when you have multiple factories that produce related objects, but the exact types of 
products depend on the factory chosen.

Example: GUI Elements for Different Platforms (Windows vs MacOS)
Suppose you're building a GUI framework that can create different types of buttons and checkboxes depending on the platform 
(e.g., Windows or MacOS). Using the Abstract Factory Pattern, you can define families of related products (buttons and checkboxes)
 and create them without specifying the exact classes.

"""

from abc import ABC, abstractmethod

# Step 1: Define Abstract Product interfaces (Button and Checkbox)
class Button(ABC):
    @abstractmethod
    def click(self):
        pass

class Checkbox(ABC):
    @abstractmethod
    def check(self):
        pass

# Step 2: Implement Concrete Products for Windows
class WindowsButton(Button):
    def click(self):
        return "Windows Button clicked"

class WindowsCheckbox(Checkbox):
    def check(self):
        return "Windows Checkbox checked"

# Step 3: Implement Concrete Products for MacOS
class MacOSButton(Button):
    def click(self):
        return "MacOS Button clicked"

class MacOSCheckbox(Checkbox):
    def check(self):
        return "MacOS Checkbox checked"

# Step 4: Define Abstract Factory
class GUIFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_checkbox(self) -> Checkbox:
        pass

# Step 5: Implement Concrete Factories for each platform
class WindowsFactory(GUIFactory):
    def create_button(self) -> Button:
        return WindowsButton()

    def create_checkbox(self) -> Checkbox:
        return WindowsCheckbox()

class MacOSFactory(GUIFactory):
    def create_button(self) -> Button:
        return MacOSButton()

    def create_checkbox(self) -> Checkbox:
        return MacOSCheckbox()

# Step 6: Client code that uses the Abstract Factory
def create_gui(factory: GUIFactory):
    button = factory.create_button()
    checkbox = factory.create_checkbox()
    
    print(button.click())
    print(checkbox.check())

# Usage Example:
# Depending on the platform, the client will choose the appropriate factory
platform = "Windows"  # Could also be "MacOS"

if platform == "Windows":
    gui_factory = WindowsFactory()
elif platform == "MacOS":
    gui_factory = MacOSFactory()
else:
    raise ValueError("Unknown platform")

create_gui(gui_factory)
