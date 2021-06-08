import random

class Code:
    def __init__(self):
        self.code = [random.randint(1,6) for x in range(4)]

    def getCode(self):
        return self.code

    def checkCode(self, code):
        wrongPositionFlag = 0
        correctPositionFlag = 0

        for i in code:
            if i in self.getCode():
                if code.index(i) == self.getCode().index(i):
                    correctPositionFlag += 1
                else:
                    wrongPositionFlag += 1

        return correctPositionFlag, wrongPositionFlag
