import random

class Code:
    def __init__(self):
        self.code = [random.randint(1,6) for x in range(4)]

    def getCode(self):
        return self.code

