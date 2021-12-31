from utils import *
from progress.bar import *
from tqdm import *
import time

def main():
    while True:
        title()
        op = int(input('>>> '))
        option(op)

def ChargingBarToClose():
    text = ' '.center(45," ")
    bar = FillingSquaresBar(text, max=100)
    for num in range(100):
        time.sleep(0.03)
        bar.next()
    bar.finish()    
    exit(0)

def option(op):
    if op == 0:
        ChargingBarToClose()