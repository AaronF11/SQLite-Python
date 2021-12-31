from os import system
from progress.bar import *
from tqdm import *
import time

spacer = "\n"
spacer_main = "\n\n\n\n\n"
# < --------------- Barras de progreso --------------- >

def ChargingBarToClose():
    system("cls")
    print(spacer_main)
    text = ' '.center(45," ")
    bar = PixelBar(text, max=100)
    for num in range(100):
        time.sleep(0.03)
        bar.next()
    bar.finish()
    system("cls")    
    exit(0)

def ChargingBarToOpen():
    system("cls")
    print(spacer_main)
    text = ' '.center(45," ")
    bar = FillingSquaresBar(text, max=100)
    for num in range(100):
        time.sleep(0.01)
        bar.next()
    bar.finish()
    system("cls")

def tqdmProgressBarSave():
    for item in tqdm(range(100)):
        time.sleep(0.01)

def tqdmProgressBarDelete():
    text = ' '.center(45," ")
    bar = FillingCirclesBar(text, max=100)
    for num in range(100):
        time.sleep(0.03)
        bar.next()
    bar.finish()


# < --------------- Titulos o encabezados --------------- >

def repeat(): #Función de código invalido| invalid code function
    system("cls")
    print("╔══════════════════════════════╗".center(127," "))
    print("║      #CÓDIGO NO VALIDO#      ║".center(127," "))
    print("╚══════════════════════════════╝".center(127," "))
    system('pause')
    
def title_menu(): #Función de titulo | Title function
    system("cls")
    print(spacer_main)
    print("╔══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╗".center(127," "))
    print("║  ║  ║  ║  ║  ║  ║  ║  ║  ║  ║  ║  ║  ║  ║  ║  ║  ║  ║  ║  ║  ║  ║  ║  ║  ║  ║".center(127," "))
    print("║  ╠══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╣  ║".center(127," "))
    print("║  ║                        BASE DE DATOS - RECORDS                        ║  ║".center(127," "))
    print("║  ╠═══════════════════════════════════╦═══════════════════════════════════╣  ║".center(127," "))
    print("║  ║     INSERTAR NUEVO REGISTRO       ║                1                  ║  ║".center(127," "))
    print("║  ╠═══════════════════════════════════╬═══════════════════════════════════╣  ║".center(127," "))
    print("║  ║    ELIMINAR REGISTRO EXISTENTE    ║                2                  ║  ║".center(127," "))
    print("║  ╠═══════════════════════════════════╬═══════════════════════════════════╣  ║".center(127," "))
    print("║  ║    MOSTRAR REGISTRO EXISTENTE     ║                3                  ║  ║".center(127," "))
    print("║  ╠═══════════════════════════════════╬═══════════════════════════════════╣  ║".center(127," "))
    print("║  ║         CERRAR PROGRAMA           ║                0                  ║  ║".center(127," "))
    print("║  ╠══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╬══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╦══╣  ║".center(127," "))
    print("║  ║  ║  ║  ║  ║  ║  ║  ║  ║  ║  ║  ║  ║  ║  ║  ║  ║  ║  ║  ║  ║  ║  ║  ║  ║  ║".center(127," "))
    print("╚══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╩══╝".center(127," "))

def title_insert(): #Función titulo de insertar  | title_insert function
    print(spacer)
    print("╔═══════════════════════════════╦════════╗".center(127," "))
    print("║            OPCIONES           ║ CÓDIGO ║".center(127," "))
    print("╠═══════════════════════════════╬════════╣".center(127," "))
    print("║    INSERTAR UNICO REGISTRO    ║    1   ║".center(127," "))
    print("╠═══════════════════════════════╬════════╣".center(127," "))
    print("║     INSERTAR MÁS REGISTROS    ║    2   ║".center(127," "))
    print("╠═══════════════════════════════╬════════╣".center(127," "))
    print("║ INSERTAR REGISTROS Y GUARDAR  ║        ║".center(127," "))
    print("║  EN UN ARCHIVO LOS REGISTROS  ║    3   ║".center(127," "))
    print("╠═══════════════════════════════╬════════╣".center(127," "))
    print("║   REGRESAR AL MENÚ PRINCIPAL  ║    0   ║".center(127," "))
    print("╚═══════════════════════════════╩════════╝".center(127," "))

def title_delete(): #Función titulo de borrar  | title_delete function
    print(spacer)
    print("╔═══════════════════════════════╦════════╗".center(127," "))
    print("║            OPCIONES           ║ CÓDIGO ║".center(127," "))
    print("╠═══════════════════════════════╬════════╣".center(127," "))
    print("║    ELIMINAR UNICO REGISTRO    ║    1   ║".center(127," "))
    print("╠═══════════════════════════════╬════════╣".center(127," "))
    print("║         ELIMINAR TODO         ║    2   ║".center(127," "))
    print("╠═══════════════════════════════╬════════╣".center(127," "))
    print("║  ELIMINAR REGISTROS Y BORRAR  ║        ║".center(127," "))
    print("║  EL ARCHIVO DE LOS REGISTROS  ║    3   ║".center(127," "))
    print("╠═══════════════════════════════╬════════╣".center(127," "))
    print("║   REGRESAR AL MENÚ PRINCIPAL  ║    0   ║".center(127," "))
    print("╚═══════════════════════════════╩════════╝".center(127," "))

def header_insert(): #Función encabezado de insertar| header_insert function
    system("cls")
    print("╔══════════════════════════════╗".center(127," "))
    print("║        INSERTAR DATOS        ║".center(127," "))
    print("╚══════════════════════════════╝".center(127," "))

def header_delete(): #Función encabezado de borrar| header_delete function
    system("cls")
    print("╔══════════════════════════════╗".center(127," "))
    print("║         BORRAR DATOS         ║".center(127," "))
    print("╚══════════════════════════════╝".center(127," "))

def header_show(): #Función encabezado de mostrar| header_show function
    system("cls")
    print("╔══════════════════════════════╗".center(127," "))
    print("║         MOSTRAR DATOS        ║".center(127," "))
    print("╚══════════════════════════════╝".center(127," "))