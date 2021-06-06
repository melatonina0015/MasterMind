from board import Board
from code import Code
from exceptions import *
import os
import random

if __name__ == '__main__':
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

    board = Board(turns)
    board.printBoard()
    '''
            print("-----------------------------------------")
            print("\t\tMenu")
            print("-----------------------------------------")
            print("Enter code using numbers.")
            print("1 - RED, 2 - GREEN, 3 - YELLOW, 4 - BLUE, 5 - BLACK, 6 - ORANGE")
            print("Example: RED YELLOW ORANGE BLACK ---> 1 3 6 5")
            print("-----------------------------------------")
            print_mastermind_board(show_passcode, guess_codes, guess_flags)

            # Accepting the player input
            try:
                code = list(map(int, input("Enter your choice = ").split()))
            except ValueError:
                clear()
                print("\tWrong choice!! Try again!!")
                continue

                # Check if the number of colors nunbers are 4
            if len(code) != 4:
                clear()
                print("\tWrong choice!! Try again!!")
                continue

            # Check if each number entered corresponds to a number
            flag = 0
            for x in code:
                if x > 6 or x < 1:
                    flag = 1

            if flag == 1:
                clear()
                print("\tWrong choice!! Try again!!")
                continue

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