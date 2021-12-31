from os import system

def title_menu(): #Función de titulo | Title function
    system("cls")
    print("\n\n\n\n\n")
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
    system("cls")
    print("\n\n\n\n\n")
    print("╔═══════════════════════════════╦════════╗".center(127," "))
    print("║            OPCIONES           ║ CÓDIGO ║".center(127," "))
    print("╠═══════════════════════════════╬════════╣".center(127," "))
    print("║    INSERTAR UNICO REGISTRO    ║    1   ║".center(127," "))
    print("╠═══════════════════════════════╬════════╣".center(127," "))
    print("║     INSERTAR MÁS REGISTROS    ║    2   ║".center(127," "))
    print("╠═══════════════════════════════╬════════╣".center(127," "))
    print("║ INSERTAR REGISTROS Y GUARDAR  ║        ║".center(127," "))
    print("║  EN UN ARCHIVO LOS REGISTROS  ║    3   ║".center(127," "))
    print("╚═══════════════════════════════╩════════╝".center(127," "))