from tkinter import *
from tkinter import ttk
from tkinter.ttk import Frame, Button, Entry, Style


class MainWindow(Frame):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.master.title("Калькулятор")

        Style().configure("TButton", padding=(0, 5, 0, 5), font='serif 10')

        self.columnconfigure(0, pad=3)
        self.columnconfigure(1, pad=3)
        self.columnconfigure(2, pad=3)
        self.columnconfigure(3, pad=3)
        self.rowconfigure(0, pad=3)
        self.rowconfigure(1, pad=3)
        self.rowconfigure(2, pad=3)
        self.rowconfigure(3, pad=3)

        editor = Entry(self)
        editor.grid(row=0, columnspan=4, sticky='we')

        btn_1 = ttk.Button(self, text="1")
        btn_1.grid(row=5, column=0)
        btn_2 = ttk.Button(self, text="2")
        btn_2.grid(row=5, column=1)
        btn_3 = ttk.Button(self, text="3")
        btn_3.grid(row=5, column=2, columnspan=1, sticky='ew')
        btn_4 = ttk.Button(self, text="4")
        btn_4.grid(row=4, column=0, columnspan=1, sticky='ew')
        btn_5 = ttk.Button(self, text="5")
        btn_5.grid(row=4, column=1, columnspan=1, sticky='ew')
        btn_6 = ttk.Button(self, text="6")
        btn_6.grid(row=4, column=2, columnspan=1, sticky='ew')
        btn_7 = ttk.Button(self, text="7")
        btn_7.grid(row=3, column=0, columnspan=1, sticky='ew')
        btn_8 = ttk.Button(self, text="8")
        btn_8.grid(row=3, column=1, columnspan=1, sticky='ew')
        btn_9 = ttk.Button(self, text="9")
        btn_9.grid(row=3, column=2, columnspan=1, sticky='ew')
        btn_0 = ttk.Button(self, text="0")
        btn_0.grid(row=6, column=1, columnspan=1, sticky='ew')

        btn_plus = ttk.Button(self, text="+")
        btn_plus.grid(row=5, column=3, columnspan=1, sticky='ew')
        btn_minus = ttk.Button(self, text="-")
        btn_minus.grid(row=4, column=3, columnspan=1, sticky='ew')
        btn_equals = ttk.Button(self, text="=")
        btn_equals.grid(row=6, column=3, columnspan=1, sticky='ew')
        btn_multiplication = ttk.Button(self, text="*")
        btn_multiplication.grid(row=3, column=3, columnspan=1, sticky='ew')
        btn_division = ttk.Button(self, text="/")
        btn_division.grid(row=2, column=3, columnspan=1, sticky='ew')
        btn_clearing = ttk.Button(self, text="AC")
        btn_clearing.grid(row=2, column=2, columnspan=1, sticky='ew')
        btn_comma = ttk.Button(self, text=",")
        btn_comma.grid(row=6, column=2, columnspan=1, sticky='ew')

        self.pack()

def main():
    root = Tk()
    root.geometry("350x500")
    MainWindow()
    root.mainloop()

