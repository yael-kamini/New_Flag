import pygame
import random
import turtle
import main
import consts
import soldier
import gamefeild
import grass
pygame.init()
def screen():
    pygame.display.set_caption("The Flag")
    screen_size = pygame.display.set_mode(
            (consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))
    screen_size.fill(consts.BACKGROUND_COLOR)
    return screen_size

print(screen())

# def draw_start_message():
#     message = consts.START_MESSAGE
#     draw_message(message,consts.START_MESSAGE_FONT_SIZE,consts.START_MESSAGE_COLOR,consts.START_MESSAGE_LOCATION)
#
#
# def draw_message(message, font_size, color, location):
#     font = pygame.font.SysFont(consts.FONT_NAME, font_size)
#     text_img = font.render(message, True, color)
#     screen.blit(text_img, location)
#
# print(draw_start_message())




# def draw_lose_message():
#     draw_message(consts.LOSE_MESSAGE, consts.LOSE_FONT_SIZE,
#                  consts.LOSE_COLOR, consts.LOSE_LOCATION)
#
#
# def draw_win_message():
#     draw_message(consts.WIN_MESSAGE, consts.WIN_FONT_SIZE,
#                  consts.WIN_COLOR, consts.WIN_LOCATION)
#
#
# def draw_message(message, font_size, color, location):
#     font = pygame.font.SysFont(consts.FONT_NAME, font_size)
#     text_img = font.render(message, True, color)
#     screen.blit(text_img, location)
#
# def draw_game(game_state):
#     if len(game_state["bubbles_popping"]):
#         pass
#     elif game_state["state"] == consts.LOSE_STATE:
#         draw_lose_message()
#
#     elif game_state["state"] == consts.WIN_STATE:
#         draw_win_message()
#
#     pygame.display.flip()

