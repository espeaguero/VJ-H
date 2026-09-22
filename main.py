import pygame

from scenes import basic_scene, game_scene, exit_scene

# ? Inicializamos pygame
pygame.init()

# ? Definimos las medidas de nuestra pantalla
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768

# ? Creamos nuestro objeto pantalla
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

jugando = True

# ? Aqui se ejecutaran las escenas del juego en orden
basic_scene.gameloop(screen)
while jugando:
    resultado_juego = game_scene.gameloop(screen)
    _, ptjs_final = resultado_juego
    resultado = exit_scene.gameloop(screen, ptjs_final)

    if resultado == "Sigue":
        jugando = True
    else:
        jugando = False
