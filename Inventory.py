import tkinter as tk
from tkinter import font
# from ttkbootstrap import Style
from tkinter import ttk
import constants as cn


class Inventory(ttk.Frame):
    def __init__(self, parent, changeGeometry):
        super().__init__(parent)

        ######################################
        # Data Capture
        self.grid_columnconfigure(
            (0, 1, 2, 3, 4, 5), weight=1, uniform="column")
        self.changeSize = changeGeometry

        self.label_1 = ttk.Label(
            self, text="INVENTARIO DE LOTES FEEDER", font="arial 14")
        self.label_1.grid(row=0, column=0, columnspan=6)
        customFont = font.Font(family="Arial", size=14)

        self.captura = ttk.Entry(self, font=customFont, width=50)
        self.captura.grid(row=1, column=0, sticky="EW",
                          pady=20, columnspan=4)

        # self.combo = ttk.Combobox(self, width=8)
        # self.combo.grid(row=1, column=3, columnspan=1,
        #                  padx=(15, 0), ipadx=10)

        self.resetButton = tk.Button(
            self, text="Opciones", font=customFont,
            command=lambda: self.changeSize("inventory"))
        self.resetButton.grid(row=1, column=4, padx=10, sticky="EW")

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
            self.statusFrame, text="0", **cn.labelConf)
        self.labelSapAmount.grid(row=1, column=0, sticky="NSEW", padx=(6, 0))

        self.label_inventario = tk.Label(
            self.statusFrame, text="INVENTARIO", **cn.labelConf)
        self.label_inventario.grid(row=0, column=1, padx=10, sticky="NSEW")

        self.labelInventarioAmount = tk.Label(
            self.statusFrame, text="0", **cn.labelConf)
        self.labelInventarioAmount.grid(
            row=1, column=1, padx=10, sticky="NSEW")

        self.label_porcentaje = tk.Label(
            self.statusFrame, text="PORCENTAJE DE INVENTARIO",
            wraplength=110, justify="center", **cn.labelConf)
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
        for i in range(4):
            self.history.heading(
                cn.columnHeadigns[i], text=cn.columnHeadigns[i])
        for i in range(4):
            self.history.column(
                cn.columnHeadigns[i], width=cn.columnWith[i], anchor="center")

        self.history.pack(expand=1, fill="both")

        self.faltantes = ttk.Treeview(self.missingTab,
                                      columns=cn.columnHeadigns,
                                      show="headings")
        for i in range(4):
            self.faltantes.heading(
                cn.columnHeadigns[i], text=cn.columnHeadigns[i])
        for i in range(4):
            self.faltantes.column(
                cn.columnHeadigns[i], width=cn.columnWith[i], anchor="center")
        self.faltantes.pack(expand=1, fill="both")

        self.tabWidget.grid(column=0, row=2, columnspan=3,
                            sticky="EW", pady=5, padx=5)
