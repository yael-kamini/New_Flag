import pygame
import main
import Screen
import consts
import gamefeild
import grass

def create_flag(flag_img):
    flag = pygame.image.load(FLAG_IMG)
    sized_flag = pygame.transform.scale(flag,(
        consts.FLAG_WIDTH,consts.FLAG_HEIGHT))
    flag_box = pygame.Sureface(
        (consts.FLAG_WIDTH,consts.FLAG_HEIGHT *2),)
    flag_box.fill(consts.GREEN)
    flag_box.blit(sized_flag,(0,0))

    return flag_box