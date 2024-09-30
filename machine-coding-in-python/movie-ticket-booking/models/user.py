class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    def set_name(self, name):
        self.name = name
    def get_name(self):
        return self.name
    def set_email(self, email):
        self.email = email
    def get_email(self):
        return self.email
    