import tkinter as tk
# from tkinter import font
from ttkbootstrap import Style
# from tkinter import ttk
# import constants as cn

from Inventory import InventoryUI
from Start import SartUI


class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Inventario Feeder')
        self.geometry('800x520')
        self.resizable(False, False)
        self.style = Style('darkly')
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True, padx=20, pady=10)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (SartUI.StartPage, InventoryUI.Inventory):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        # Show The First Page
        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

    def changeGeometry(self, window):
        if window == "inventory":
            self.geometry('800x520')
        else:
            self.geometry('800x800')


if __name__ == '__main__':
    Application().mainloop()
