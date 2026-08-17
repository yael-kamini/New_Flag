import pygame
import random
import main
import Screen
import consts
import soldier
import gamefeild
import mine

def create_grass(grass_img):
    grass = pygame.image.load(consts.GRASS_IMG)
    sized_grass = pygame.transform.scale(grass,(
        consts.GRASS_WIDTH,consts.GRASS_HEIGHT))
    grass_box = pygame.Sureface(
        (consts.GRASS_WIDTH,consts.GRASS_HEIGHT *2),)
    grass_box.fill(consts.GREEN)
    grass_box.blit(sized_grass,(0,0))

    return grass_box


