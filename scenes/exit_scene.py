import pygame
from pygame.locals import K_ESCAPE, KEYDOWN, QUIT, K_RETURN

def gameloop(screen, ptjs_final=0):

    # Inicializamos el reloj
    clock = pygame.time.Clock()

    running = True

    background_image = pygame.image.load("assets/fondo_exit.png").convert()
    image_scaled = pygame.transform.scale(background_image, (screen.get_width(), screen.get_height()))

    # Definimos la fuente y texto a usar
    font = pygame.font.SysFont("Chalkboard SE", 48)
    line1 = font.render("Perdiste...", True, (255, 255, 255))
    line2 = font.render("Aprieta ESC para salir del juego,", True, (255, 255, 255))
    line3 = font.render("o enter para jugar denuevo", True, (255, 255, 255))
    line4 = font.render(f"Puntaje final: {ptjs_final}", True, (255, 255, 255))

    # Definimos las posiciones de los textos
    line1_rect = line1.get_rect(
        center=(screen.get_width() // 2, screen.get_height() // 2 - 25)
    )

    line2_rect = line2.get_rect(
        center=(screen.get_width() // 2, screen.get_height() // 2 + 25)
    )

    line3_rect = line3.get_rect(
        center=(screen.get_width() // 2, screen.get_height() // 2 + 75)
    )

    line4_rect = line4.get_rect(
        center=(screen.get_width() // 2, screen.get_height() // 2 + 125)
    )

    # Iniciamos el loop principal de la escena inicial
    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                elif event.key == K_RETURN:
                    return "Sigue"
            elif event.type == QUIT:
                running = False

        screen.blit(image_scaled, (0, 0))

        # Dibujar textos
        screen.blit(line1, line1_rect)
        screen.blit(line2, line2_rect)
        screen.blit(line3, line3_rect)
        screen.blit(line4, line4_rect)

        # Actualizar pantalla
        pygame.display.flip()

        # Limitar FPS
        clock.tick(30)
