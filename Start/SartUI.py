import tkinter as tk
from tkinter import font
from tkinter import ttk


class StartPage(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.controller = controller

        customFont = font.Font(family="Arial", size=40, slant="italic")
        self.label = tk.Label(
            self, text="Inventario Mensual Feeder", font=customFont)
        # font=controller.title_font)
        self.label.pack(side="top", fill="x", pady=(150, 20))

        buttonFont = font.Font(family="Arial", size=20, slant="italic")
        self.button1 = tk.Button(self, text="Inicio", font=buttonFont, padx=60,
                                 command=lambda: controller.show_frame("Inventory"))
        self.button1.pack(pady=10)
