import tkinter as tk
from tkinter import font
from tkinter import ttk
from tkinter import filedialog as fd
from pathlib import Path
from . import functions as fn
from . import constants as cn


class Admin(ttk.Frame):
    def __init__(self, parent, controller, path):
        super().__init__(parent)

        self.controller = controller
        self.rootPath = path
        self.database = fn.getDatabase(self.rootPath)

        self.filename = ""

        self.grid_columnconfigure(
            (0, 1, 2, 3, 4, 5), weight=1, uniform="column")

        customFont = font.Font(family="Arial", size=20, slant="italic")
        self.label = tk.Label(
            self, text="Subir Wip", font="Arial 40")
        # font=controller.title_font)
        self.label.grid(row=0, column=0, columnspan=6, pady=(20, 30))

        self.directory = tk.Label(self, font=customFont, **cn.labelConf)
        self.directory.grid(row=1, column=0, columnspan=5,
                            sticky="NSEW", padx=(0, 10), pady=(0, 40))

        buttonFont = font.Font(family="Arial", size=20, slant="italic")
        self.button1 = tk.Button(self, text="Buscar", font=buttonFont, padx=0,
                                 command=self.searchForFile)
        self.button1.grid(row=1, column=5, columnspan=1,
                          sticky="EW", pady=(0, 40))

        self.monthLabel = tk.Label(self, text="Mes", font="Arial 20")
        self.monthLabel.grid(row=4, column=0, columnspan=1)
        self.monthEntry = tk.Entry(self, justify="center", font="Arial 20")
        self.monthEntry.grid(row=4, column=1, sticky="NS")

        self.yearLabel = tk.Label(self, text="Año", font="Arial 20")
        self.yearLabel.grid(row=4, column=2, columnspan=1)
        self.yearEntry = tk.Entry(self, justify="center", font="Arial 20")
        self.yearEntry.grid(row=4, column=3, sticky="NS")

        self.button1 = tk.Button(self, text="Subir", font=buttonFont, padx=0,
                                 command=self.uploadData)
        self.button1.grid(row=4, column=4, columnspan=2,
                          sticky="EW", padx=(40, 0))

        self.statusLabel = tk.Label(self, text="", fg="red", font="Arial 20")
        self.statusLabel.grid(row=5, column=0, columnspan=6, pady=(20, 0))

    def searchForFile(self):
        filetypes = (
            ('excel file', '*.xlsx'),
            ('All files', '*.*')
        )
        filename = fd.askopenfilename(
            title="Buscar Archivo",
            initialdir=f"{Path.home()}/Documents",
            filetypes=filetypes
        )
        self.filename = filename
        truncated = self.filename.split("/")[-1]
        self.directory.config(text=truncated)

    def uploadData(self):
        month = self.monthEntry.get()
        year = self.yearEntry.get()
        date = month + year
        exist = fn.ceckDatabase(date, self.database)
        if exist:
            self.statusLabel.config(
                text="Ya existen datos en la fecha.", fg="red")
            return

        if self.filename == "":
            self.statusLabel.config(
                text="Debes selecionar un archivo.", fg="red")
            return
        if month == "":
            self.statusLabel.config(
                text="Debes introducir el mes.", fg="red")
            return
        if year == "":
            self.statusLabel.config(
                text="Debes introducir el año.", fg="red")
            return
        fn.insertIntoDb(self.filename, cn.columns,
                        self.database, date, cn.area)
        self.statusLabel.config(
            text="Los datos se cargaron exitosamente.", fg="green")
