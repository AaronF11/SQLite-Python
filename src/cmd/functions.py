from utils import *
from sql.connection import *
from msvcrt import getch

# < --------------- main --------------- >

def main():
    while True:
        title_menu()
        op = int(input('>>> '))
        menu_option(op)


# < --------------- Funciones de menú y elegir opción "insertar" --------------- >

def option_insert():
    header_insert()
    title_insert()
    op_insert = int(input('>>> '))
    menu_insert(op_insert)

def menu_insert(op_insert):
    if op_insert == 1:
        one_insert()

    elif op_insert == 2:
        two_insert()

    elif op_insert == 3:
        three_insert()
    
    elif op_insert == 0:
        ChargingBarToClose()
        main()

    else:
        repeat()
        option_insert()

def one_insert():
    header_insert()
    requirements()
    option_insert()

def two_insert():
    header_insert()
    print('CANTIDAD DE REGISTROS A INGRESAR')
    loop = int(input('>>> '))
    for i in range(loop):
        requirements()
    option_insert()
    
def three_insert():
    header_insert()
    print('CANTIDAD DE REGISTROS A INGRESAR')
    loop = int(input('>>> '))
    for i in range(loop):
        makefile()
    option_insert()

def requirements():
    connection = sqlite3.connect("src/database/database.db")
    cursor = connection.cursor()

    print('INGRESA LA MATRICULA')
    enrollment = str(input('>>> '))
    print('INGRESA EL NOMBRE')
    name = str(input('>>> ')).upper()
    print('INGRESA LOS APELLIDOS')
    lastnames = str(input('>>> ')).upper()
    print('INGRESA EL CORREO INSTITUCIONAL')
    mail = str(input('>>> ')).lower()
    
    insert_into = """INSERT INTO records (MATRICULA, NOMBRE, APELLIDOS, CORREO_INSTITUCIONAL) VALUES (?, ?, ?, ?)"""
    values = (enrollment , name, lastnames, mail)
    cursor.execute(insert_into,values)
    cursor.close()
    connection.commit()
    connection.close()

    tqdmProgressBarSave()

def makefile():
    connection = sqlite3.connect("src/database/database.db")
    cursor = connection.cursor()

    print('INGRESA LA MATRICULA')
    enrollment = str(input('>>> '))
    print('INGRESA EL NOMBRE')
    name = str(input('>>> ')).upper()
    print('INGRESA LOS APELLIDOS')
    lastnames = str(input('>>> ')).upper()
    print('INGRESA EL CORREO INSTITUCIONAL')
    mail = str(input('>>> ')).lower()
    
    file = open('src/txt/records.txt', 'a')
    include_enrollment = ' MATRICULA : ' + enrollment
    include_name = ' NOMBRE : ' + name
    include_lastnames = ' APELLIDOS : ' + lastnames
    include_mail = ' CORREO INSTITUCIONAL : ' + mail
    file.write('| ')
    file.write(include_enrollment)
    file.write(' | ')
    file.write(include_name)
    file.write(' | ')
    file.write(include_lastnames)
    file.write(' | ')
    file.write(include_mail)
    file.write(' | ')
    file.write('\n')
    file.close()

    insert_into = """INSERT INTO records (MATRICULA, NOMBRE, APELLIDOS, CORREO_INSTITUCIONAL) VALUES (?, ?, ?, ?)"""
    values = (enrollment , name, lastnames, mail)
    cursor.execute(insert_into,values)
    cursor.close()
    connection.commit()
    connection.close()

    tqdmProgressBarSave()
    
    
# < --------------- Funciones de menú y elegir opción "eliminar" --------------- >

def option_delete():
    header_delete()
    title_delete()
    op_delete = int(input('>>> '))
    menu_delete(op_delete)

def menu_delete(op_delete):
    if op_delete == 1:
        one_delete()

    elif op_delete == 2:
        two_delete()

    elif op_delete == 3:
        three_delete()

    elif op_delete == 0:
        ChargingBarToClose()
        main()

    else:
        repeat()
        option_delete()

def one_delete():
    header_delete()
    connection = sqlite3.connect("src/database/database.db")
    cursor = connection.cursor()

    delete = "DELETE FROM records WHERE MATRICULA = ?"
    print('INGRESA LA MATRICULA')
    enrollment = str(input('>>> '))
            
    adr = (enrollment, )
    cursor.execute(delete, adr)
    cursor.close()
    connection.commit()
    connection.close()
    tqdmProgressBarDelete()
    option_delete()

def two_delete():
    header_delete()
    connection = sqlite3.connect("src/database/database.db")
    cursor = connection.cursor()

    delete = "DELETE FROM records"
    cursor.execute(delete)
    cursor.close()
    connection.commit()
    connection.close()
    tqdmProgressBarDelete()
    option_delete()

def three_delete():
    header_delete()
    connection = sqlite3.connect("src/database/database.db")
    cursor = connection.cursor()
    delete = "DELETE FROM records"
    cursor.execute(delete)
    cursor.close()
    connection.commit()
    connection.close()
    tqdmProgressBarDelete()

    file = open('src/txt/records.txt', 'w')
    file.truncate()
    file.close()
    option_delete()


# < --------------- Funciones de menú y elegir opción "mostrar" --------------- >
def option_show():
    header_show()
    title_show()
    op_show = int(input('>>> '))
    menu_show(op_show)

def menu_show(op_show):
    if op_show == 1:
        one_show()

    elif op_show == 2:
        two_show()

    elif op_show == 3:
        three_show()

    elif op_show == 0:
        ChargingBarToClose()
        main()

    else:
        repeat()
        option_show()

def one_show():
    header_show()
    show_db()
    getch()
    option_show()

def two_show():
    header_show()
    show_file()
    getch()
    option_show()


def three_show():
    header_show()
    show_db()
    show_file()
    getch()
    option_show()

def show_db():
    connection = sqlite3.connect("src/database/database.db")
    cursor = connection.cursor()

    select_tables = "SELECT name FROM sqlite_master WHERE type='table'"
    cursor.execute(select_tables)
    tables = cursor.fetchall()
    show_tables()
    for names in tables:
        print(names)
    
    select_records = "SELECT * FROM records"
    cursor.execute(select_records)
    records = cursor.fetchall()

    cursor.close()
    connection.close()

    show_records()
    for files in records:
        print(files)

def show_file():
    show_records_file()
    file = open('src/txt/records.txt')
    print(file.read())
    file.close()

# < --------------- Funciones de menú principal--------------- >
def menu_option(op):
    if op == 0:
        ChargingBarToClose()
        exit(0)
        
    if op == 1:
        ChargingBarToOpen()
        option_insert()

    if op == 2:
        ChargingBarToOpen()
        option_delete()
    
    if op == 3:
        ChargingBarToOpen()
        option_show()

    else:
        repeat()