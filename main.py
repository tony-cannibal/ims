import tkinter as tk
# from tkinter import font
from ttkbootstrap import Style
# from tkinter import ttk
# import constants as cn

from Inventory import Inventory


class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Inventario Feeder')
        self.geometry('800x520')
        self.resizable(False, False)
        self.style = Style('darkly')
        self.Inventory = Inventory(self, self.changeGeometry)
        self.Inventory.pack(padx=20, pady=10)

    def changeGeometry(self, window):
        if window == "inventory":
            self.geometry('800x520')
        else:
            self.geometry('800x800')


if __name__ == '__main__':
    Application().mainloop()
