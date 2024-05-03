import pygame as pg
from sudoku_utils import Sudoku

#Setup constants
FPS = 30


def setup():
    #This function extracts all of the setup from main
    sudoku = Sudoku()
    sudoku.generate_sudoku()
    global clock
    clock = pg.time.Clock()

    pass

def draw():
    #Draw frame
    pass

def main():
    #Setup
    setup()
    while True:
        #Loop
        clock.tick(FPS)
        #First we handle player input
        #Then we apply game logic
        #Then we display
        draw() #Draw once every loop
        pass