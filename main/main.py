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
                os.system("cls")
                print("Zła wartość!")
                continue

                # Check if the number of numbers are 4
            if len(userCode) != 4:
                os.system("cls")
                print("Zła długość kodu!")
                continue

                # Check if each number entered corresponds to a number
            flag = 0
            for x in userCode:
                if x > 6 or x < 1:
                    flag = 1

            if flag == 1:
                os.system("cls")
                print("Elementy kodu są za duże lub za małe!")
                continue
            break

        board.setCodeFlag(userCode, turn)
        board.printBoard(userCode, turn)



    '''
            print("-----------------------------------------")
            print("\t\tMenu")
            print("-----------------------------------------")
            print("Enter code using numbers.")
            print("1 - RED, 2 - GREEN, 3 - YELLOW, 4 - BLUE, 5 - BLACK, 6 - ORANGE")
            print("Example: RED YELLOW ORANGE BLACK ---> 1 3 6 5")
            print("-----------------------------------------")
            print_mastermind_board(show_passcode, guess_codes, guess_flags)


                # Storing the player input
            for i in range(4):
                guess_codes[turn][i] = colors_map[code[i]]

                # Process to apply clues according to the player input
            dummy_passcode = [x for x in passcode]

            pos = 0

            # Loop to set up clues for the player move
            for x in code:
                if colors_map[x] in dummy_passcode:
                    if code.index(x) == passcode.index(colors_map[x]):
                        guess_flags[turn][pos] = 'R'
                    else:
                        guess_flags[turn][pos] = 'W'
                    pos += 1
                    dummy_passcode.remove(colors_map[x])

            random.shuffle(guess_flags[turn])

            # Check for win condition
            if guess_codes[turn] == passcode:
                clear()
                print_mastermind_board(passcode, guess_codes, guess_flags)
                print("Congratulations!! YOU WIN!!!!")
                break

            # Update turn
            turn += 1
            clear()

    # Check for loss condiiton
    if turn == chances:
        clear()
        print_mastermind_board(passcode, guess_codes, guess_flags)
        print("YOU LOSE!!! Better luck next time!!!")
        
    '''''