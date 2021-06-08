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

    kod = Code()
    board = Board(turns)

    for turn in range(turns):
        while(True):
            try:
                userCode = list(map(int, input("Wprowadź kod = ").split()))
                if len(userCode) != 4:
                    raise wrongCodeLength
                for x in userCode:
                    if x > 6 or x < 1:
                        raise numberOutOfRange
                break
            except wrongCodeLength:
                print("Zła długość kodu!")
            except numberOutOfRange:
                print("Elementy kodu są za duże lub za małe!")
            except ValueError:
                print("Zła wartość!")

        board.printBoard(userCode, turn)