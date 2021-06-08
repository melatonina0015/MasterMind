from board import Board
from code import Code
from exceptions import *
from os import system, name
import random

if __name__ == '__main__':

    def clear():

        # for windows
        if name == 'nt':
            _ = system('cls')

        # for mac and linux(here, os.name is 'posix')
        else:
            _ = system('clear')

    while(True):
        try:
            turns = int(input("Podaj liczbe tur (8-12):"))
            if turns < 8:
                raise valueTooSmallException
            elif turns > 12:
                raise valueTooLargeException
            break
        except valueTooSmallException:
            print("Za mało rund")
        except valueTooLargeException:
            print("Za dużo rund")
        except ValueError:
            print("Zła wartość!")

    clear()

    kod = Code()
    board = Board(turns)

    for turn in range(turns):
        while(True):
            try:
                userCode = list(map(int, input("Wprowadź kod = ").split()))
            except ValueError:
                clear()
                print("Zła wartość!")
                continue

                # Check if the number of numbers are 4
            if len(userCode) != 4:
                clear()
                print("Zła długość kodu!")
                continue

                # Check if each number entered corresponds to a number
            flag = 0
            for x in userCode:
                if x > 6 or x < 1:
                    flag = 1

            if flag == 1:
                clear()
                print("Elementy kodu są za duże lub za małe!")
                continue
            break

        board.setCodeFlag(userCode, turn)
        board.printBoard(userCode, turn)