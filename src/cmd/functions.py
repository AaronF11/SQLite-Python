from utils import *
from progress.bar import *
from tqdm import *
import time

def main():
    while True:
        title_menu()
        op = int(input('>>> '))
        menu_option(op)


def ChargingBarToClose():
    text = ' '.center(45," ")
    bar = FillingSquaresBar(text, max=100)
    for num in range(100):
        time.sleep(0.03)
        bar.next()
    bar.finish()
    system("cls")    
    exit(0)

def ChargingBarToOpen():
    text = ' '.center(45," ")
    bar = PixelBar(text, max=100)
    for num in range(100):
        time.sleep(0.01)
        bar.next()
    bar.finish()
    system("cls")  


def menu_insert(op_insert):
    if op_insert == 1:
        pass

    elif op_insert == 2:
        pass

    elif op_insert == 3:
        pass
    
    elif op_insert == 0:
        pass

    else:
        repeat()
        option_insert()
        
def option_insert():
    title_insert()
    op_insert = int(input('>>> '))
    menu_insert(op_insert)


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

def option_delete():
    title_delete()
    op_delete = int(input('>>> '))
    menu_delete(op_delete)


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