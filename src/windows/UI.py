from funtions import *
from tkinter import * 
import tkinter
import sqlite3

def main():
    color_widgets = "white"
    color_background_frame = "orange"
    color_background_root = "whitesmoke"
    color_letters = "black"

    root = Tk()
    root.title("BASE DE DATOS - RECORDS")
    #root.geometry("550x400")
    #root.resizable(0,0)
    root.iconbitmap("src/windows/ico/database.ico")

    menu = Menu(root)
    menu.configure(
                background = color_widgets,
                foreground = color_letters)
    root.configure(background = color_background_root)
    root.config(menu = menu)

    frame = Frame(root)
    frame.configure(
                    background = color_background_frame,
                    relief = "groove",
                    borderwidth = 3,
                    pady= 10
                    )
    frame.grid(row = 1, column = 1)
    
    frame_two = Frame(root)
    frame_two.configure(
                    background = color_background_frame,
                    relief = "groove",
                    borderwidth = 3,
                    pady = 10
                    )
    frame_two.grid(row = 2, column = 1)
    
    frame_three = Frame(root)
    frame_three.configure(
                    background = color_background_frame,
                    relief = "groove",
                    borderwidth = 3,
                    pady = 10
                    )

    db = Menu(menu, tearoff = 0)
    db.configure(
                background = color_widgets,
                foreground = color_letters)
    db.add_command(label = "NUEVO REGISTRO")
    db.add_command(label = "BUSCAR REGISTRO")
    db.add_command(label = "CERRAR", command = end)
    
    editor = Menu(menu, tearoff = 0)
    editor.configure(
                background = color_widgets,
                foreground = color_letters)
    editor.add_command(label = "MODIFICAR REGISTRO")
    editor.add_command(label = "ELIMINAR REGISTRO")
    
    about = Menu(menu, tearoff = 0)
    about.configure(
                background = color_widgets,
                foreground = color_letters)
    about.add_command(label = "ACERCA DE", command = info_about)

    menu.add_cascade(label = "ARCHIVO", menu = db)
    menu.add_cascade(label = "EDITAR", menu = editor)
    menu.add_cascade(label = "ACERCA DE", menu = about)
    
    # < --------------- 1 row --------------- >
    var_id = StringVar()
    
    label_id = Label(frame, text = "CÓDIGO :")
    label_id.configure(
                    foreground = color_letters,
                    background = color_background_frame
                    )
    label_id.grid(
                row = 1,
                column = 1,
                sticky = W,
                padx = 10,
                pady = 10
                )
    
    entry_id = Entry(frame, textvariable = var_id)
    entry_id.configure(
                        width = 38,
                        borderwidth = 2, 
                        relief = "ridge"
                        )
    entry_id.grid(
                row = 1,
                column = 2,
                sticky = W,
                padx = 10,
                pady = 10
                )

    # < --------------- 2 row --------------- >
    var_name = StringVar()
    
    label_name = Label(frame, text = "NOMBRE :")
    label_name.configure(
                    foreground = color_letters,
                    background = color_background_frame
                    )
    label_name.grid(
                row = 2,
                column = 1,
                sticky = W,
                padx = 10,
                pady = 10
                )
    
    entry_name = Entry(frame, textvariable = var_name)
    entry_name.configure(
                        width = 38,
                        borderwidth = 2, 
                        relief = "ridge"
                        )
    entry_name.grid(
                row = 2,
                column = 2,
                sticky = W,
                padx = 10,
                pady = 10
                )

    # < --------------- 3 row --------------- >
    var_lastname = StringVar()
    
    label_lastname = Label(frame, text = "APELLIDO :")
    label_lastname.configure(
                    foreground = color_letters,
                    background = color_background_frame
                    )
    label_lastname.grid(
                row = 3,
                column = 1,
                sticky = W,
                padx = 10,
                pady = 10
                )
    
    entry_lastname = Entry(frame, textvariable = var_lastname)
    entry_lastname.configure(
                        width = 38,
                        borderwidth = 2, 
                        relief = "ridge"
                        )
    entry_lastname.grid(
                row = 3,
                column = 2,
                sticky = W,
                padx = 10,
                pady = 10
                )
    
    # < --------------- 4 row --------------- >
    var_mail = StringVar()
    
    label_mail = Label(frame, text = "CORREO :")
    label_mail.configure(
                    foreground = color_letters,
                    background = color_background_frame
                    )
    label_mail.grid(
                row = 4,
                column = 1,
                sticky = W,
                padx = 10,
                pady = 10
                )
    
    entry_mail = Entry(frame, textvariable = var_mail)
    entry_mail.configure(
                        width = 38,
                        borderwidth = 2, 
                        relief = "ridge"
                        )
    entry_mail.grid(
                row = 4,
                column = 2,
                sticky = W,
                padx = 10,
                pady = 10
                )

    # < --------------- Buttons --------------- >
    button_new = Button(frame_two, text = "NUEVO REGISTRO")
    button_new.configure(
                        background = color_widgets,
                        foreground = color_letters,
                        borderwidth = 2, 
                        relief = "raised",
                        width = 20, 
                        command = new
                        )
    button_new.grid(
                row = 1,
                column = 1,
                sticky = W,
                padx = 10,
                pady = 10
                )

    button_search = Button(frame_two, text = "BUSCAR REGISTRO")
    button_search.configure(
                        background = color_widgets,
                        foreground = color_letters,
                        borderwidth = 2, 
                        relief = "raised",
                        width = 20, 
                        command = search
                        )
    button_search.grid(
                row = 1,
                column = 2,
                sticky = W,
                padx = 10,
                pady = 10
                )
    
    button_update = Button(frame_two, text = "MODIFICAR REGISTRO")
    button_update.configure(
                        background = color_widgets,
                        foreground = color_letters,
                        borderwidth = 2, 
                        relief = "raised",
                        width = 20, 
                        command = update
                        )
    button_update.grid(
                row = 2,
                column = 1,
                sticky = W,
                padx = 10,
                pady = 10
                )
    
    button_delete = Button(frame_two, text = "ELIMINAR REGISTRO")
    button_delete.configure(
                        background = color_widgets,
                        foreground = color_letters,
                        borderwidth = 2, 
                        relief = "raised",
                        width = 20, 
                        command = delete
                        )
    button_delete.grid(
                row = 2,
                column = 2,
                sticky = W,
                padx = 10,
                pady = 10
                )
    
    button_clear = Button(frame_two, text = "LIMPIAR")
    button_clear.configure(
                        background = color_widgets,
                        foreground = color_letters,
                        borderwidth = 2, 
                        relief = "raised",
                        width = 20, 
                        command = clear
                        )
    button_clear.grid(
                row = 3,
                column = 1,
                sticky = W,
                padx = 10,
                pady = 10
                )

    button_close = Button(frame_two, text = "CERRAR")
    button_close.configure(
                        background = color_widgets,
                        foreground = color_letters,
                        borderwidth = 2, 
                        relief = "raised",
                        width = 20, 
                        command = close
                        )
    button_close.grid(
                row = 3,
                column = 2,
                sticky = W,
                padx = 10,
                pady = 10
                )

    # < --------------- TextBox row --------------- >
    """ text = Text(frame, height = 10, width = 42)
    text.grid(
            row = 5,
            column = 1,
            columnspan= 2,
            sticky = W,
            padx = 2,
            pady = 2
            ) """

    root.mainloop()