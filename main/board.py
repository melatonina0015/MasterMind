from code import Code

class Board(Code):
    def __init__(self,szanse):
        self.correctPositionFlag = ['-' for x in range(szanse)]
        self.wrongPositionFlag = ['-' for x in range(szanse)]
        self.guess_codes = [['-', '-', '-', '-'] for x in range(szanse)]
        self.szanse = szanse
        self.kod = Code()

    def setCodeFlag(self, code, turn):
        for i in range(4):
            self.guess_codes[-(turn+1)][i] = code[i]

    def printBoard(self):
        """
        Metoda wypisuje plansze do gry
        """
        print("-" * 40)
        print("MASTERMIND".center(40))
        print("-" * 40)
        print("WP CP |", end="")

        for x in range(4):
            print("NUM".center(8), end='')
        print()

        for i in range(self.szanse):
            print("-" * 40)
            print(self.correctPositionFlag[i], "", self.wrongPositionFlag[i], " |", end ='')
            for x in self.guess_codes[i]:
                print(str(x).center(8), end="")
            print()
        print("-" * 40)
