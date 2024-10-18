"""
The Singleton pattern is a creational design pattern that ensures a class has only one instance
and provides a global point of access to that instance. 
It's useful when exactly one object is needed to coordinate actions across the system.
"""

class Singleton:
    _instance = None 

    def __new__(self):
        if self._instance is None:
            self._instance = super(Singleton, self).__new__(self)
        return self._instance
    
    def some_business_logic():
        pass

s1 = Singleton()
s2 = Singleton()
print(s1 is s2)