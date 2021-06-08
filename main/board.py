from code import Code

class Board(Code):
    def __init__(self, turns):
        """

        :param szanse:
        """
        self.correctPositionFlag = ['-' for x in range(turns)]
        self.wrongPositionFlag = ['-' for x in range(turns)]
        self.guess_codes = [['-', '-', '-', '-'] for x in range(turns)]
        self.turns = turns
        self.kod = Code()

    def setCodeFlag(self, userCode, turn):
        """

        :param userCode:
        :param turn:
        """
        for i in range(4):
            self.guess_codes[-(turn+1)][i] = userCode[i]

    def printBoard(self, userCode, turn):
        """
        Metoda wypisuje plansze do gry
        """
        self.setCodeFlag(userCode, turn)

        print("-" * 40)
        print("MASTERMIND".center(40))
        print("-" * 40)
        print("CP WP |", end="")

        for x in range(4):
            print("NUM".center(8), end='')
        print()

        for i in range(self.turns):

            self.correctPositionFlag[-(turn+1)], self.wrongPositionFlag[-(turn+1)] = self.kod.checkCode(userCode)
            self.guess_codes[-(turn+1)] = userCode
            print("-" * 40)
            print(self.correctPositionFlag[i], "", self.wrongPositionFlag[i], " |", end ='')
            for x in self.guess_codes[i]:
                print(str(x).center(8), end="")
            print()
        print("-" * 40)

        if userCode == self.kod.getCode():
            print("Congratulations!! YOU WIN!!!!")
            exit()

        if turn == self.turns-1:
            print("YOU LOSE!!!!")
            exit()

