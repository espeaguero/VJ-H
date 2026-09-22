if __name__ == "__main__":
    raise RuntimeError("\033c❌ ESTE ARCHIVO NO DEBE EJECUTARSE. EJECUTA main.py")

import pygame
from pygame.locals import K_ESCAPE, KEYDOWN, MOUSEBUTTONDOWN, QUIT

from elements import Enemy, Player, Mirilla


def gameloop(screen):
    # * Preparamos la escena de juego, cargando los elementos que se van a usar en el loop principal

    # ? Añadir fondo del display
    background_image = pygame.image.load("assets/background.png").convert()

    # ? Crear la instancia de jugador
    player = Player(screen)

    # ? Crear los grupos de sprites
    enemies = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)

    # ? Crear el generador de enemigos
    ADDENEMY = pygame.USEREVENT + 1
    pygame.time.set_timer(ADDENEMY, 600)

    # ? Crear el reloj del juego
    clock = pygame.time.Clock()

    pygame.mixer.music.load("assets/loop.WAV")
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(-1)

    sonido_disparo = pygame.mixer.Sound("assets/disparo.wav")
    sonido_disparo.set_volume(0.6)
    sonido_explosion = pygame.mixer.Sound("assets/enemigos.wav")

    #Tablero vidas
    hud_font = pygame.font.SysFont("Chalkboard SE", 28)

    # Creamos mirilla
    mirilla = Mirilla()

    running = True  # variable booleana para manejar el loop
    juego_terminado = False

    # * Loop principal del juego, todo lo que ocurre en el juego se hace dentro de este loop
    while running:
        # ? Dibujar la imagen de fondo en la ventana
        screen.blit(background_image, (0, 0))

        # Iteramos sobre cada evento en la cola
        for event in pygame.event.get():
            if event.type == KEYDOWN:  # se presiono una tecla?
                if event.key == K_ESCAPE:  # era la tecla de escape?
                    running = False  # terminamos el loop

            elif event.type == QUIT:  # fue un click al cierre de la ventana?
                running = False  # terminamos el loop

            # ? Generar enemigos
            elif event.type == ADDENEMY:
                new_enemy = Enemy(screen)
                enemies.add(new_enemy)
                all_sprites.add(new_enemy)

            # TODO (2.5): Disparar balas al hacer click con el mouse
            elif event.type == MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                player.shoot(mouse_pos)
                sonido_disparo.play()

        # ? Actualizar el estado interno de los sprites (posiciones, etc)
        pressed_keys = pygame.key.get_pressed()
        player.update(pressed_keys)
        enemies.update()
        mirilla.update()

        # ? Dibujar los sprites actualizados en la ventana
        for entity in all_sprites:
            screen.blit(entity.image, entity.rect)

        # TODO (2.5): Dibujar las balas en la ventana
        for bullet in player.bullets:
            screen.blit(bullet.image, bullet.rect)

        # ? Calcular colisiones entre jugador y enemigos + perder vidas
        enemigo_chocado = pygame.sprite.spritecollideany(player, enemies)
        if enemigo_chocado and not player.invulnerable:
            enemigo_chocado.kill()
            juego_terminado = player.recibir_dano()
            if juego_terminado:
                running = False
        
        screen.blit(mirilla.image, mirilla.rect)

        # TODO (2.6): Calcular colisiones entre balas y enemigos
        eliminados = pygame.sprite.groupcollide(
            player.bullets,
            enemies,
            True,
            True,
        )

        if eliminados:
            sonido_explosion.play()

        for lista_enemigos in eliminados.values():
            player.sumar_ptjs(len(lista_enemigos) * 10)

        #Texto vidas
        texto_ptjs = hud_font.render(f"Puntaje: {player.ptjs}", True, (255, 255, 255))
        texto_vidas = hud_font.render(f"Vidas: {player.vidas}", True, (255, 255, 255))
        screen.blit(texto_ptjs, (10, 10))
        screen.blit(texto_vidas, (10, 40))

        # ? Actualizar la ventana para reflejar todos los cambios
        pygame.display.flip()

        # ? Controlar la velocidad de fotogramas
        clock.tick(60)

    if juego_terminado:
        return "Perdiste", player.ptjs
    return "Sigue", player.ptjs

