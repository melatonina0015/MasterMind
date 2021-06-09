from tkinter import *
from tkinter import messagebox
from board import Board
from code import Code
from exceptions import *
from os import system, name
import random

if __name__ == '__main__':
    '''
    def mainWindow():
        def check():
            userCode = []
            userCode.append(int(float(entry1.get())))
            userCode.append(int(float(entry2.get())))
            userCode.append(int(float(entry3.get())))
            userCode.append(int(float(entry4.get())))

            messagebox.showinfo(message=userCode)

        
        while (True):
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
            while (True):
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
            


        tury = int(float(e.get()))
        root = Tk()
        root.title("MasterMind")

        labelMastermind = Label(root, text="MasterMind").grid(row=0, column=1, columnspan=4)
        labelCorrectPosition = Label(root, text="Dobra pozycja").grid(row=0, column=0)
        labelWrongPosition = Label(root, text="Zła pozycja").grid(row=0, column=5)

        labelMastermindArr = []
        labelCorrectPositionArr = []
        labelWrongPositionArr = []
        for i in range(tury):
            labelCorrectPositionArr.append((Label(root, text="-").grid(row=i + 1, column=0)))
            labelWrongPositionArr.append((Label(root, text="-").grid(row=i + 1, column=5)))

        for i in range(tury * 4):
            labelMastermindArr.append(Label(root, text="-").grid(row=int(i / 4) + 1, column=(i % 4) + 1))

        entry1 = Entry(root, width=10).grid(row=tury + 2, column=1)
        entry2 = Entry(root, width=10).grid(row=tury + 2, column=2)
        entry3 = Entry(root, width=10).grid(row=tury + 2, column=3)
        entry4 = Entry(root, width=10).grid(row=tury + 2, column=4)

        button1Frame2 = Button(root, text="Sprawdź kod", command = check, ).grid(row=tury + 3, column=2, columnspan=2)

        root.mainloop()

    def exception1():
        turns = int(float(e.get()))
        if turns < 8:
            messagebox.showerror(message="Za mało rund")
        elif turns > 12:
            messagebox.showerror(message="Za duzo rund")
        else:
            mainWindow()

    prolog = Tk()
    prolog.title("MasterMind")

    e = Entry(prolog, width = 30)
    e.pack()
    e.insert(0, "Podaj liczbe tur (8-12):")
    b = Button(prolog, text = "Potwierdz", command = exception1).pack()

    prolog.mainloop()
    '''

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