class Memory:

    def __init__(self):
        self.logs = []

    def add(self, message):
        self.logs.append(message)

    def get(self):
        return self.logs