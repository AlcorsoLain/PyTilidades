from tkinter import *
from PIL import ImageTk, Image
from tkinter.ttk import *
from Clases.calculadora import app
#icon
root = Tk()
root.title("-----")
root.geometry("425x508")
root.mainloop()
# stuff you want to do
root.after(10000, app())