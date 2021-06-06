from code import Code

class Board(Code):
    def __init__(self,szanse):
        self.guess_flags = [['-', '-', '-', '-'] for x in range(szanse)]
        self.guess_codes = [['-', '-', '-', '-'] for x in range(szanse)]
        self.szanse = szanse
        self.kod = Code()

    def printBoard(self):
        """
        Metoda wypisuje plansze do gry
        """
        print("-" * 40)
        print("MASTERMIND".center(40))
        print("-" * 40)
        print("    |", end="")

        for x in range(4):
            print("NUM".center(8), end='')
        print()

        for i in range(self.szanse):
            print("-" * 40)
            print(self.guess_flags[i][0], self.guess_flags[i][1], "|")
            print(self.guess_flags[i][2], self.guess_flags[i][3], end=" |")
            for x in self.guess_codes[i]:
                print(x.center(8), end="")
            print()
        print("-" * 40)
