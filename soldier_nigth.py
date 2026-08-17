import pygame
import main
import Screen
import consts
import gamefeild
import grass
def create_night_solider(night_soldier_img):
    night_soldier = pygame.image.load(night_soldier_img)
    sized_night_soldier = pygame.transform.scale(night_soldier,(
        consts.NIGHT_SOLDIER_WIDTH,consts.NIGHT_SOLDIER_HEIGHT))
    night_soldier_box = pygame.Sureface(
        (consts.NIGHT_SOLDIER_WIDTH,consts.NIGHT_SOLDIER_HEIGHT *2),)
    night_soldier_box.fill(consts.BACKGROUND_COLOR)
    night_soldier_box.blit(sized_night_soldier,(0,0))

    return night_soldier_box