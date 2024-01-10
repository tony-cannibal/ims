import tkinter as tk
from tkinter import font
# from ttkbootstrap import Style
from tkinter import ttk
from datetime import date
from . import constants as cn
from . import functions as fn


class Inventory(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.area = "M1"
        self.mes = date.today().strftime("%m%y")
        self.wip = fn.getWip(cn.database, self.area, self.mes)
        self.wipLength = len(self.wip)
        self.inventory = {}

        ######################################
        # Data Capture
        self.grid_columnconfigure(
            (0, 1, 2, 3, 4, 5), weight=1, uniform="column")

        self.label_1 = ttk.Label(
            self, text="INVENTARIO DE LOTES FEEDER", font="arial 14")
        self.label_1.grid(row=0, column=0, columnspan=6)
        customFont = font.Font(family="Arial", size=14)

        self.captura = ttk.Entry(self, font=customFont, width=50)
        self.captura.grid(row=1, column=0, sticky="EW",
                          pady=20, columnspan=4)

        self.captura.bind('<Return>', self.captureItem)

        # self.combo = ttk.Combobox(self, width=8)
        # self.combo.grid(row=1, column=3, columnspan=1,
        #                  padx=(15, 0), ipadx=10)

        self.optionButton = tk.Button(
            self, text="Opciones", font=customFont,
            command=lambda: controller.show_frame("StartPage"))
        self.optionButton.grid(row=1, column=4, padx=10, sticky="EW")

        self.configButton = tk.Button(
            self, text="Configuracion", font=customFont,
            command=lambda: self.changeSize("other"))
        self.configButton.grid(row=1, column=5, sticky="EW")

        #######################################
        # Labels

        self.statusFrame = ttk.LabelFrame(self, text="Status")
        self.statusFrame.grid(column=0, row=4, columnspan=6, sticky="EW")

        self.statusFrame.grid_columnconfigure(
            (0, 1, 2), weight=1, uniform="column")

        self.label_sap = tk.Label(
            self.statusFrame, text="SAP", background="#666", **cn.labelConf)
        self.label_sap.grid(row=0, column=0, sticky="NSEW", padx=(6, 0))
        self.labelSapAmount = tk.Label(
            self.statusFrame, text=self.wipLength, **cn.labelConf)
        self.labelSapAmount.grid(row=1, column=0, sticky="NSEW", padx=(6, 0))

        self.label_inventario = tk.Label(
            self.statusFrame, text="INVENTARIO", background="#666",
            **cn.labelConf)
        self.label_inventario.grid(row=0, column=1, padx=10, sticky="NSEW")

        self.labelInventarioAmount = tk.Label(
            self.statusFrame, text="0", **cn.labelConf)
        self.labelInventarioAmount.grid(
            row=1, column=1, padx=10, sticky="NSEW")

        self.label_porcentaje = tk.Label(
            self.statusFrame, text="PORCENTAJE DE INVENTARIO",
            background="#666", wraplength=110, justify="center",
            **cn.labelConf)
        self.label_porcentaje.grid(row=0, column=2, sticky="NSEW", padx=(0, 6))

        self.labelPorcentajeAmount = tk.Label(
            self.statusFrame, text="0",
            wraplength=110, justify="center", **cn.labelConf)
        self.labelPorcentajeAmount.grid(
            row=1, column=2, sticky="NSEW", padx=(0, 6))

        ###############################################
        # Tables

        self.tabWidget = ttk.Notebook(self.statusFrame)

        self.progressTab = ttk.Frame(self.tabWidget)
        self.missingTab = ttk.Frame(self.tabWidget)

        self.tabWidget.add(self.progressTab, text="Escaneado")
        self.tabWidget.add(self.missingTab, text="Faltantes")

        self.history = ttk.Treeview(self.progressTab,
                                    columns=cn.columnHeadigns, show="headings")
        for i in range(5):
            self.history.heading(
                cn.columnHeadigns[i], text=cn.columnHeadigns[i])
        for i in range(5):
            self.history.column(
                cn.columnHeadigns[i], width=cn.columnWith[i], anchor="center")

        self.history.pack(expand=1, fill="both")

        self.faltantes = ttk.Treeview(self.missingTab,
                                      columns=cn.columnHeadigns,
                                      show="headings")
        for i in range(5):
            self.faltantes.heading(
                cn.columnHeadigns[i], text=cn.columnHeadigns[i])
        for i in range(5):
            self.faltantes.column(
                cn.columnHeadigns[i], width=cn.columnWith[i], anchor="center")
        self.faltantes.pack(expand=1, fill="both")

        self.tabWidget.grid(column=0, row=2, columnspan=3,
                            sticky="EW", pady=5, padx=5)

    ##############################################################
    # set
        self.updateTables()

    ##############################################################
    # Functions

    def getText(self, event):
        codigo = self.captura.get()
        self.captura.delete(0, 'end')
        codigo = fn.checkCode(codigo)
        print(codigo)

    def updateTables(self):
        self.history.delete(*self.history.get_children())
        self.inventory = fn.getInventory(cn.database, self.area, self.mes)
        for i in self.inventory:
            self.history.insert('', tk.END, values=(
                self.inventory[i][1],
                self.inventory[i][2],
                self.inventory[i][3],
                self.inventory[i][4],
                self.inventory[i][5]
            ))

        for i in self.wip:
            if i not in self.inventory:
                self.faltantes.insert('', tk.END, values=(
                    self.wip[i][10],
                    self.wip[i][3],
                    self.wip[i][12],
                    self.wip[i][5],
                    self.wip[i][11]
                ))

    def captureItem(self, event):
        codigo = self.captura.get()
        self.captura.delete(0, 'end')
        codigo = fn.checkCode(codigo)
        if codigo == "err":
            return
        if codigo in self.wip:
            if codigo not in self.inventory:
                record = [
                    self.mes + self.wip[codigo][10],
                    self.wip[codigo][10],
                    self.wip[codigo][3],
                    self.wip[codigo][12],
                    self.wip[codigo][5],
                    self.wip[codigo][11],
                    self.wip[codigo][14],
                ]
                fn.captureRecord(record, self.mes, cn.database)
                self.updateTables()
                print("Record Saved")
            else:
                print("Record Not Saved")

        else:
            print("not in inventory")
