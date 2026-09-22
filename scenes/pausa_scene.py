import pygame


def gameloop(screen):
    clock = pygame.time.Clock()
    fuente = pygame.font.Font(None, 48)

    titulo = fuente.render("Pausa", True, (255, 255, 255))
    reanudar = fuente.render("Reanudar", True, (255, 255, 255))
    salir = fuente.render("Salir", True, (255, 255, 255))

    centro_x = screen.get_width() // 2

    titulo_rect = titulo.get_rect(center=(centro_x, 250))
    reanudar_rect = reanudar.get_rect(center=(centro_x, 350))
    salir_rect = salir.get_rect(center=(centro_x, 430))

    fondo = pygame.image.load("assets/fondo_exit.png").convert()
    fondo = pygame.transform.scale(fondo, screen.get_size())

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "salir"

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return "reanudar"

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if reanudar_rect.collidepoint(event.pos):
                        return "reanudar"
                    if salir_rect.collidepoint(event.pos):
                        return "salir"

        screen.blit(fondo, (0, 0))
        screen.blit(titulo, titulo_rect)
        screen.blit(reanudar, reanudar_rect)
        screen.blit(salir, salir_rect)

        pygame.display.flip()
        clock.tick(30)