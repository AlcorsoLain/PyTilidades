import tkinter as tk
from tkinter import ttk

#clase contr0ls, declara los controles

class contr0ls(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.Label1 = ttk.Label(parent, text="Bienvenido a PYtilidades")
        self.Label1.place(x=20,y=20)
        self.Btn_Calculator = ttk.Button(parent, text="Calculadora")
        self.Btn_Calculator.place(x=30,y=50)


#Iniciacion de Tkinter
main = tk.Tk()
main.title("PYtilidades")
main.geometry("400x300")
app = contr0ls(main)
main.mainloop()
