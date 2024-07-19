from tkinter import *
from tkinter import ttk


class MainWindow(object):
    def __init__(self):
        root = Tk()
        root.title("Калькулятор")
        root.geometry("500x700")

        editor = Text(height=15)
        editor.grid(sticky="EW")

        btn_1 = ttk.Button(text="1")
        btn_1.grid()
        btn_2 = ttk.Button(text="2")
        btn_2.grid()
        btn_3 = ttk.Button(text="3")
        btn_3.grid()
        btn_4 = ttk.Button(text="4")
        btn_4.grid()
        btn_5 = ttk.Button(text="5")
        btn_5.grid()
        btn_6 = ttk.Button(text="6")
        btn_6.grid()
        btn_7 = ttk.Button(text="7")
        btn_7.grid()
        btn_8 = ttk.Button(text="8")
        btn_8.grid()
        btn_9 = ttk.Button(text="9")
        btn_9.grid()
        btn_0 = ttk.Button(text="0")
        btn_0.grid()

        btn_plus = ttk.Button(text="+")
        btn_plus.grid()
        btn_minus = ttk.Button(text="-")
        btn_minus.grid()
        btn_equals = ttk.Button(text="=")
        btn_equals.grid()
        btn_multiplication = ttk.Button(text="*")
        btn_multiplication.grid()
        btn_division = ttk.Button(text="/")
        btn_division.grid()
        btn_clearing = ttk.Button(text="AC")
        btn_clearing.grid()
        btn_comma = ttk.Button(text=",")
        btn_comma.grid()

        root.mainloop()

