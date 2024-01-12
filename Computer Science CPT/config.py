import pygame

pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")

BG = pygame.image.load("Background.png")

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("Corporation Games.otf", size)