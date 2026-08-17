import pygame
import main
import Screen
import consts
import gamefeild
import grass
import mine

def create_night_solider(night_soldier_img):
    night_soldier = pygame.image.load(consts.SOLDIER_NIGHT_IMG)
    sized_night_soldier = pygame.transform.scale(night_soldier,(
        consts.SOLDIER_NIGHT_WIDTH,consts.SOLDIER_NIGHT_HEIGHT))
    night_soldier_box = pygame.Sureface(
        (consts.SOLDIER_NIGHT_WIDTH,consts.SOLDIER_NIGHT_HEIGHT *2),)
    night_soldier_box.fill(consts.GREEN)
    night_soldier_box.blit(sized_night_soldier,(0,0))

    return night_soldier_box
