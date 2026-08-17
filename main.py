import sys
import pygame
import game_field
import soldier
import consts
import screen


state = {
    "original_soldier": screen.soldier(consts.SOLDIER_IMG),
    "is_soldier_moved": False,
    "is_window_open": True,
    "state": consts.RUNNING_STATE,
}

def main():
    pygame.init()

def handle_user_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state["is_window_open"] = False
            sys.exit()

        elif state["state"] != consts.RUNNING_STATE:
            continue

    consts.SOLDIER_X , consts.SOLDIER_Y = 0 , 0
    vel = 10
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and consts.WINDOW_WIDTH > 0:
        consts.SOLDIER_X -= vel
    if keys[pygame.K_RIGHT] and consts.WINDOW_WIDTH < 500 - consts.SOLDIER_WIDTH:
        consts.SOLDIER_X += vel
    if keys[pygame.K_UP] and consts.WINDOW_HEIGHT > 0:
        consts.SOLDIER_Y -= vel
    if keys[pygame.K_DOWN] and consts.WINDOW_HEIGHT < 250 - consts.SOLDIER_HEIGHT :
        consts.SOLDIER_Y += vel
    pygame.display.update()

    # if consts.SOLDIER_X > consts.WINDOW_WIDTH - consts.SOLDIER_WIDTH or consts.SOLDIER_X < 0:


    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                screen.dark_screen() #shelly?


def move_player(grid, row, col):
    new_row = consts.SOLDIER_Y + 1
    new_col = consts.SOLDIER_X + 1
    if 'is_soldier_moved':
        return new_row, new_col



# main():
#     while ("is_window_open")