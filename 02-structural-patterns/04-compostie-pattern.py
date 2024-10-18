"""
The Composite Pattern is a structural design pattern that allows you to compose objects into tree-like 
structures to represent part-whole hierarchies. It treats individual objects and compositions of objects uniformly, 
meaning that you can interact with both single objects and composites (groups of objects) in the same way.

Key Concepts:
Component: An interface or abstract class that defines the operations that can be performed on both simple and composite objects.
Leaf: Represents a single object that does not have any children. It implements the Component interface.
Composite: A class that represents a group of Leaf objects or other composites. It implements the Component interface and provides methods for adding, removing, and interacting with child components.
When to Use:
When you want to represent part-whole hierarchies of objects.
When you need to treat individual objects and compositions of objects uniformly.
When the structure can be nested recursively.
Example Scenarios:
File System: Files and folders, where folders can contain files and other folders.
UI Components: Buttons, text fields, and panels, where panels can contain other UI elements, including buttons and text fields.
"""

from abc import ABC, abstractmethod

#Component interface
class FileComponent(ABC):
    @abstractmethod
    def show_details(self):
        pass

# Leaf Class
class File(FileComponent):
    def __init__(self, name) -> None:
        self.name = name
    def show_details(self):
        print(f"File {self.name}")

#Composite class

class Directory(FileComponent):
    def __init__(self, name):
        self.name = name
        self.childrens = []
    def add(self, file_component):
        self.childrens.append(file_component)
    def remove(self, file_component):
        self.childrens.remove(file_component)
    def show_details(self):
        print(f"Directory: {self.name}")
        for child in self.childrens:
            child.show_details()


# Usage
if __name__ == "__main__":
    file1 = File("file1.txt")
    file2 = File("file2.txt")

    directory = Directory("Documents")
    directory.add(file1)
    directory.add(file2)

    root_directory = Directory("Root")
    root_directory.add(directory)

    root_directory.show_details()