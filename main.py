import pygame

from scenes import basic_scene, game_scene, exit_scene, inicio_scene

# ? Inicializamos pygame
pygame.init()

# ? Definimos las medidas de nuestra pantalla
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768

# ? Creamos nuestro objeto pantalla
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

resultado = inicio_scene.gameloop(screen)
jugando = resultado == "comenzar"

while jugando:
    game_scene.gameloop(screen)
    resultado = exit_scene.gameloop(screen)
    jugando = resultado == "Sigue"

pygame.quit()
