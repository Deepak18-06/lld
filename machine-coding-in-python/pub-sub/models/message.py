class Message:
    def __init__(self, id, content):
        self.id = id
        self.content = content

    def get_content(self):
        return self.content