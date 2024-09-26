"""
The Proxy Design Pattern is a structural design pattern that provides a surrogate or placeholder 
for another object to control access to it. A proxy controls access to the real object by allowing you 
to perform additional actions (such as lazy initialization, access control, logging, or caching) before or 
after interacting with the real object.

Types of Proxies:
Virtual Proxy: Delays the creation and initialization of an object until it's actually needed (lazy 
initialization).
Protection Proxy: Controls access to the real object, typically used for security purposes.
Remote Proxy: Manages interaction with an object that exists in a different address space (e.g., 
 accessing a remote server).
Caching Proxy: Caches the results of expensive operations to improve performance.
"""


from abc import ABC, abstractmethod

# Step 1: Define the common interface (Subject)
class Image(ABC):
    @abstractmethod
    def display(self):
        pass

# Step 2: Implement the Real Object (RealSubject)
class RealImage(Image):
    def __init__(self, filename: str):
        self.filename = filename
        self._load_image_from_disk()

    def _load_image_from_disk(self):
        print(f"Loading image from {self.filename}...")

    def display(self):
        print(f"Displaying {self.filename}")

# Step 3: Implement the Proxy (that controls access to the RealImage)
class ProxyImage(Image):
    def __init__(self, filename: str):
        self.filename = filename
        self._real_image = None  # RealImage will be created only when needed

    def display(self):
        if self._real_image is None:
            self._real_image = RealImage(self.filename)  # Lazy initialization
        self._real_image.display()

# Step 4: Client code
# Usage without proxy
print("Without proxy:")
real_image = RealImage("photo1.jpg")
real_image.display()  # Outputs: Loading image from photo1.jpg, then Displaying photo1.jpg

# Usage with proxy
print("\nWith proxy:")
proxy_image = ProxyImage("photo2.jpg")
print("Image not loaded yet.")
proxy_image.display()  # Outputs: Loading image from photo2.jpg, then Displaying photo2.jpg
proxy_image.display()  # Outputs: Displaying photo2.jpg (image is already loaded)
