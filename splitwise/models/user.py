class User:
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email
    def setName(self, name: str) -> None:
        self.name = name
    def getName(self) -> str:
        return self.name
    def setEmail(self, email: str) -> None:
        self.email = email
    def getEmail(self) -> str:
        return self.email
    