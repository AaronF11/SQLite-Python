from utils import *
from sql.connection import *

# < --------------- main --------------- >

def main():
    while True:
        title_menu()
        op = int(input('>>> '))
        menu_option(op)


# < --------------- Funciones de menú y elegir opción "insertar" --------------- >

def option_insert():
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
        pass

    else:
        repeat()
        option_insert()

def one_insert():
    header_insert()
    requirements()

def two_insert():
    header_insert()
    print('CANTIDAD DE REGISTROS A INGRESAR')
    loop = int(input('>>> '))
    for i in range(loop):
        requirements()
    
def three_insert():
    header_insert()
    print('CANTIDAD DE REGISTROS A INGRESAR')
    loop = int(input('>>> '))
    for i in range(loop):
        makefile()

def requirements():
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

    tqdmProgressBar()

def makefile():
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

    tqdmProgressBar()
    
    
# < --------------- Funciones de menú y elegir opción "eliminar" --------------- >

def option_delete():
    title_delete()
    op_delete = int(input('>>> '))
    menu_delete(op_delete)

def menu_delete(op_delete):
    if op_delete == 1:
        pass

    elif op_delete == 2:
        pass

    elif op_delete == 3:
        pass

    elif op_delete == 0:
        pass

    else:
        repeat()
        option_delete()

def one_delete():
    header_delete()

def two_delete():
    header_delete()

def three_delete():
    header_delete()

    
# < --------------- Funciones de menú principal--------------- >
def menu_option(op):
    if op == 0:
        ChargingBarToClose()
        
    elif op == 1:
        ChargingBarToOpen()
        option_insert()

    elif op == 2:
        ChargingBarToOpen()
        option_delete()

    elif op == 3:
        pass

    elif op == 0:
        exit(0)

    else:
        repeat()