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
        self.correctPositionFlag = 0
        self.wrongPositionFlag = 0
        self.mastermindLabel = Label(self.master, text = 'MasterMind')
        self.dobraPozycjaLabel = Label(self.master, text = 'Cyfry na dobrej pozycji')
        self.zlaPozycjaLabel = Label(self.master, text = 'Cyfry na złej pozycji')
        self.zlaPozycja = [Label(self.master, text = '-') for i in range(self.rundy)]
        self.dobraPozycja = [Label(self.master, text='-') for i in range(self.rundy)]
        self.pusteOdpowiedzi = [Label(self.master, text = '-') for i in range(self.rundy * 4)]
        self.wejscia = [Entry(self.master, width = 10) for i in range(4)]
        self.przycisk = Button(self.master, text = "Spawdź kod", command = lambda : self.sprawdzKod())

        self.dobraPozycjaLabel.grid(row = 0, column = 0)
        self.mastermindLabel.grid(row = 0, column = 1, columnspan = 4)
        self.zlaPozycjaLabel.grid(row = 0, column = 5)
        for i in range(self.rundy * 4):
            self.pusteOdpowiedzi[i].grid(row = int(i/4)+1, column = (i % 4)+1)
        for i in range(self.rundy):
            self.zlaPozycja[i].grid(row = i+1, column = 0)
            self.dobraPozycja[i].grid(row = i+1, column = 5)
        for i in range(4):
            self.wejscia[i].grid(row = self.rundy+1, column = i + 1)
        self.przycisk.grid(row = self.rundy + 3, column = 1, columnspan = 4)

        print(self.odp)

    def sprawdzKod(self):
        self.kodGracza = []
        for i in range(4):
            self.kodGracza.append(int(self.wejscia[i].get()))

        for i in range(4):
            self.odpowiedzi = [(Label(self.master, text=self.kodGracza[i])) for i in range(4)]
            self.odpowiedzi[i].grid(row= self.rundy, column = i+1)

        self.ustawFlagi()
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

    def ustawFlagi(self):
        self.correctPositionFlag = 0
        self.wrongPositionFlag = 0
        
        for i in range(4):
            if self.kodGracza[i] in self.odp:
                if self.kodGracza[i] == self.odp[i]:
                    self.correctPositionFlag += 1
                else:
                    self.wrongPositionFlag += 1

        self.flagaDobraPozycja = Label(self.master, text = self.correctPositionFlag)
        self.flagaZlaPozycja = Label(self.master, text = self.wrongPositionFlag)

        self.flagaDobraPozycja.grid(row = self.rundy, column = 0)
        self.flagaZlaPozycja.grid(row = self.rundy, column = 5)









tk = Tk()
gui = FirstWindow(tk)
tk.mainloop()