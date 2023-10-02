import tkinter
from ttkbootstrap import Style
from tkinter import ttk


class Application(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.title('Inventario Feeder')
        self.geometry('610x780')
        self.style = Style('journal')
        self.login = Login(self, "Hello There.")
        self.login.pack()


class Login(ttk.Frame):
    def __init__(self, parent, string):
        super().__init__(parent)

        self.label_1 = ttk.Label(self, text=string, padding=10)
        self.label_1.grid(row=0, column=0)
        self.padding = 10

        self.button_1 = ttk.Button(self, text="Im a Button")
        self.button_1.grid(row=1, column=0)


if __name__ == '__main__':
    Application().mainloop()
