import pygame
import random
import main
import Screen
import consts
import soldier
import gamefeild

def create_mine(grass_img):
    mine = pygame.image.load(consts.MINE_IMG)
    sized_mine = pygame.transform.scale(mine,(
        consts.MINE_WIDTH,consts.MINE_HEIGHT))
    mine_box = pygame.Sureface(
        (consts.MINE_WIDTH,consts.MINE_HEIGHT *2),)
    mine_box.fill(consts.GREEN)
    mine_box.blit(sized_mine,(0,0))

    return mine_box
