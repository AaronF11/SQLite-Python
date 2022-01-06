from UI import *
from tkinter import messagebox

def info_about():
    messagebox.showinfo("Acerca de", "version 03/01/2022")

def warning():
    messagebox.showwarning("Aviso", "Acción no guardada")

def end():
    answer = messagebox.askquestion("Cerrar", "Desea finalizar el programa")
    if answer == "yes":
        exit(0)
    else:
        pass

def new():
    print("hola")

def search():
    pass

def update():
    pass

def delete():
    pass

def clear():
    pass

def close():
    pass