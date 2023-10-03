import tkinter as tk
from tkinter import font
from ttkbootstrap import Style
from tkinter import ttk
import constants as cn


class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Inventario Feeder')
        self.geometry('800x500')
        self.resizable(False, False)
        self.style = Style('journal')
        self.Inventory = Inventory(self, self.changeGeometry)
        self.Inventory.pack(padx=20, pady=10)

    def changeGeometry(self, window):
        if window == "inventory":
            self.geometry('800x500')
        else:
            self.geometry('800x800')


class Inventory(ttk.Frame):
    def __init__(self, parent, changeGeometry):
        super().__init__(parent)

        self.grid_columnconfigure(
            (0, 1, 2, 3, 4, 5), weight=1, uniform="column")
        self.changeSize = changeGeometry

        self.label_1 = ttk.Label(
            self, text="INVENTARIO DE LOTES FEEDER", font="arial 14")
        self.label_1.grid(row=0, column=0, columnspan=6)
        customFont = font.Font(family="Arial", size=14)

        self.captura = ttk.Entry(self, font=customFont, width=50)
        self.captura.grid(row=1, column=0, sticky="EW",
                          pady=20, padx=(0, 10), columnspan=4)

        # self.combo = ttk.Combobox(self, width=8)
        # self.combo.grid(row=1, column=3, columnspan=1, padx=(15, 0), ipadx=10)

        self.resetButton = ttk.Button(
            self, text="Reset", command=lambda: self.changeSize("inventory"))
        self.resetButton.grid(row=1, column=4, padx=10)

        self.configButton = ttk.Button(
            self, text="config", command=lambda: self.changeSize("other"))
        self.configButton.grid(row=1, column=5)

        #######################################

        self.statusFrame = ttk.LabelFrame(self, text="Status")
        self.statusFrame.grid(column=0, row=4, columnspan=6, sticky="EW")

        self.statusFrame.grid_columnconfigure(
            (0, 1, 2), weight=1, uniform="column")

        self.label_sap = ttk.Label(
            self.statusFrame, text="SAP", font=cn.fontLable)
        self.label_sap.grid(row=0, column=0)

        self.label_inventario = ttk.Label(
            self.statusFrame, text="INVENTARIO", font=cn.fontLable)
        self.label_inventario.grid(row=0, column=1, padx=10)

        self.label_porcentaje = ttk.Label(
            self.statusFrame, text="PORCENTAJE DE INVENTARIO",
            wraplength=110, justify="center", font=cn.fontLable)
        self.label_porcentaje.grid(row=0, column=2, )


if __name__ == '__main__':
    Application().mainloop()
