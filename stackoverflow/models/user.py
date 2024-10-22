class User:
    def __init__(self, name, email) -> None:
        self.name = name 
        self.email = email

    def get_name (self):
        return self.name
    def set_name(self,name):
        self.name = name