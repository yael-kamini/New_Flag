import array
import random
import numpy as np
import pygame
import random
from numpy import size
import main
import Screen
import consts
import soldier
import grass

bored_game = []
def create_bored_game_matrix():
    rows = consts.BORED_ROW
    col = consts.BORED_COL

    for i in range(rows):
        row = []
        for j in range(col):
            row.append("EMPTY")
        bored_game.append(row)

    for i in range(rows):
        for j in range(col):
            print(bored_game[i][j], end=" ")
        print()
    return bored_game



def does_cell_in_bored_empty():
    create_bored_game_matrix()
    for row in range(len(bored_game)):
        for col in range(len(bored_game[row])):
            if bored_game[row][col] == "EMPTY":
                return True
    return False

def chose_a_random_cell(bored_game):
    matrix = bored_game
    import random
    for i in range(20):
        x = random.randint(0, consts.BORED_COL)
        y = random.randint(0, consts.BORED_ROW)
        value = matrix[y][x]
    return value

def create_bored(value, matrix):
    matrix = bored_game
    cell = value
    if cell is does_cell_in_bored_empty():
        create_grass()
    return matrix

def create_dark_bored():
    matrix = bored_game
    cell = value
    if cell is does_cell_in_bored_empty():# and not in the erea of the flag and solider:
        create_mine()
    return bored_game
