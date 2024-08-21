class Class:
    _instance = None
    
    def __init__(self):
        self.variables = {}

    @staticmethod
    def get_instance():
        if Class._instance is None:
            Class._instance = Class()
        return Class._instance
    
    def get_value(self, key):
        return self.variables.get(key, "")
    
    def put_value(self, key, value):
        self.variables[key] = value




