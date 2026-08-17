import pygame
import main
import Screen
import consts
import gamefeild
import grass
import mine
pygame.init()

def create_solider(soldier_img):
    soldier = pygame.image.load(consts.SOLDIER_IMG)
    sized_soldier = pygame.transform.scale(soldier,(
        consts.SOLDIER_WIDTH,consts.SOLDIER_HEIGHT))
    soldier_box = pygame.Sureface(
        (consts.SOLDIER_WIDTH,consts.SOLDIER_HEIGHT *2),)
    soldier_box.fill(consts.GREEN)
    soldier_box.blit(sized_soldier,(0,0))

    return soldier_box




