import pygame

mirillaPNG = pygame.image.load("assets/mirilla.png")
mirillaPNG_scaled = pygame.transform.scale(mirillaPNG,(50,50))

class Mirilla(pygame.sprite.Sprite):
    def __init__(self):

        self.image = mirillaPNG_scaled
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.center = pygame.mouse.get_pos()