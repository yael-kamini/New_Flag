import pygame
import sys
import random
import turtle
import time
import main
import consts
import soldier
import gamefeild
import grass
import mine
pygame.init()

def screen():
    global screen_size
    pygame.display.set_caption("The Flag")
    screen_size = pygame.display.set_mode(
            (consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))
    screen_size.fill(consts.GREEN)


def drawGrid():
    blocksize = 10
    for row in range(0,consts.WINDOW_WIDTH,blocksize):
        for col in range(0,consts.WINDOW_HEIGHT,blocksize):
            rect = pygame.Rect(row,col,blocksize,blocksize)
            pygame.draw.rect(screensize,consts.WHITE,rect,1)

def draw_message(message, font_size, color, location):
    font = pygame.font.SysFont(consts.FONT_NAME, font_size)
    text_img = font.render(message, True, color)
    screen_size.blit(text_img, location)
    time.sleep(3)

def draw_start_message():
    message = consts.START_MESSAGE
    draw_message(message,consts.START_MESSAGE_FONT_SIZE,consts.START_MESSAGE_COLOR,consts.START_MESSAGE_LOCATION)

print(screen())
print(draw_start_message())




def draw_lose_message():
    draw_message(consts.LOSE_MESSAGE, consts.FONT_SIZE,
                 consts.LOSE_COLOR, consts.LOSE_LOCATION)


def draw_win_message():
    draw_message(consts.WIN_MESSAGE, consts.FONT_SIZE,
                 consts.WIN_COLOR, consts.WIN_LOCATION)



def draw_game(game_state):
    if game_state["state"] == consts.RUNNING_STATE:
        draw_start_message()
    elif game_state["state"] == consts.LOSE_STATE:
        draw_lose_message()
        time.sleep(3)
        exit
    elif game_state["state"] == consts.WIN_STATE:
        raw_win_message()
        time.sleep(3)
        exit
    pygame.display.flip()


# ככה שלי עשתה את המסך אם שלנו לא יעבוד אפשר להעזר
# screen = pygame.display.set_mode((WINDOW_WIDTH , WINDOW_HEIGHT))
# color = GREEN
# screen.fill(color)
# pygame.display.flip()
# time.sleep(4)

