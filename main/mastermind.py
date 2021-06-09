import random
from tkinter import *
from tkinter import messagebox

class FirstWindow:
    def __init__(self, master):
        self.master = master
        self.rundyEntry = Entry(master, width=30)
        self.potwierdz = Button(master, text="Potwierdz", command = self.initMasterMind)

        self.rundy = IntVar()

        self.rundyEntry.insert(0, "Podaj liczbe rund (8-12):")
        self.rundyEntry.pack()
        self.potwierdz.pack()

    def initMasterMind(self):
        self.rundy = int(self.rundyEntry.get())

        mastermind = Tk()
        window = MasterMind(mastermind, self.rundy)
        mastermind.mainloop()


class MasterMind:
    def __init__(self, master, rundy):
        self.master = master
        self.rundy = rundy
        self.odp = [random.randint(1,6) for i in range(4)]
        self.kodGracza = []
        self.pusteOdpowiedzi = [Label(self.master, text = '-') for i in range(self.rundy * 4)]
        self.wejscia = [Entry(self.master, width = 10) for i in range(4)]
        self.przycisk = Button(self.master, text = "Spawdź kod", command = lambda : self.sprawdzKod())

        for i in range(self.rundy * 4):
            self.pusteOdpowiedzi[i].grid(row = int(i/4), column = i % 4)
        for i in range(4):
            self.wejscia[i].grid(row = self.rundy, column = i)
        self.przycisk.grid(row = self.rundy + 1, column = 1, columnspan = 2)

        print(self.odp)

    def sprawdzKod(self):
        self.kodGracza = []
        for i in range(4):
            self.kodGracza.append(int(self.wejscia[i].get()))

        for i in range(4):
            self.odpowiedzi = [(Label(self.master, text=self.kodGracza[i])) for i in range(4)]
            self.odpowiedzi[i].grid(row= self.rundy - 1, column = i)

        self.czyWygrana()
        self.rundy -= 1

    def czyWygrana(self):
        print(self.odp)
        print(self.kodGracza)
        if self.kodGracza == self.odp:
            messagebox.showinfo("Wygrana!", "Udało Ci się w " + str(self.rundy) + " rundzie!")
            exit()

        if self.rundy-1 == 0:
            messagebox.showinfo("Przegrana!", "Poprawny kod to: " + str(self.odp))
            exit()





tk = Tk()
gui = FirstWindow(tk)
tk.mainloop()