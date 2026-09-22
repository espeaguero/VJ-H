import pygame


def gameloop(screen):
    clock = pygame.time.Clock()

    fondo = pygame.image.load("assets/fondo_exit.png").convert()
    fondo = pygame.transform.scale(fondo, screen.get_size())

    texto_titulo = "VIDEOJUEGO"
    texto_subtitulo = "¡Ayuda a Jorge y su patito a escapar de las cucarachas!"

    fuente_titulo = pygame.font.Font(None, 64)
    fuente_subtitulo = pygame.font.Font(None, 36)

    titulo = fuente_titulo.render(
        texto_titulo, True, (255, 255, 255)
    )
    subtitulo = fuente_subtitulo.render(
        texto_subtitulo, True, (255, 255, 255)
    )

    titulo_rect = titulo.get_rect(
        center=(screen.get_width() // 2, 180)
    )
    subtitulo_rect = subtitulo.get_rect(
        center=(screen.get_width() // 2, 240)
    )

    boton = pygame.Rect(312, 350, 400, 60)
    texto_boton = fuente_subtitulo.render(
        "Click para comenzar", True, (255, 255, 255)
    )

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "salir"

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return "salir"

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and boton.collidepoint(event.pos):
                    return "comenzar"

        screen.blit(fondo, (0, 0))
        screen.blit(titulo, titulo_rect)
        screen.blit(subtitulo, subtitulo_rect)

        pygame.draw.rect(screen, (80, 80, 80), boton)
        screen.blit(
            texto_boton,
            texto_boton.get_rect(center=boton.center)
        )
        pygame.display.flip()
        clock.tick(30)