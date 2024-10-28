from abc import ABC, abstractmethod

class BaseRepo:
    def __init__(self):
        self.model = {}

    def find(self, id):
        self.model.get(id, None)

    def find_by(self, attribute):
        return [entry for key, entry in self.model if self.model.attribute == attribute]
    
    