from utils import *
from progress.bar import *
from tqdm import *
import time

def main():
    while True:
        title_menu()
        op = int(input('>>> '))
        option(op)

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
        time.sleep(0.03)
        bar.next()
    bar.finish()
    system("cls")  

def option(op):
    if op == 0:
        ChargingBarToClose()
    
    elif op == 1:
        ChargingBarToOpen()
        title_insert()
        op_insert = int(input('>>> '))
        
    elif op == 2:
        pass

    elif op == 3:
        pass

    else:
        pass