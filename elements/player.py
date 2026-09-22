if __name__ == "__main__":
    raise RuntimeError("\033c❌ ESTE ARCHIVO NO DEBE EJECUTARSE. EJECUTA main.py")

import math

import pygame
from pygame.locals import K_a, K_d, K_s, K_w
from pygame.math import Vector2

from elements import Bullet

JorgePNG = pygame.image.load("assets/jorge.png")
JorgePNG_scaled = pygame.transform.scale(JorgePNG, (80, 80))


class Player(pygame.sprite.Sprite):
    def __init__(self, screen):

        # ? super().__init__() inicializa la clase padre (Sprite)
        super().__init__()

        self.image = JorgePNG_scaled
        self.rect = self.image.get_rect()
        self.screen_width = screen.get_width()
        self.screen_height = screen.get_height()

        # TODO (2.4): Crear grupo de balas
        self.bullets = pygame.sprite.Group()

        self.habilitado = True
        self.ultimo_disparo = 0
        self.cooldown = 2000

        # Vidas y puntaje del jugador
        self.vidas = 3
        self.ptjs = 0

        # Para que no se quede pegado en un mismo choque todo el rato
        self.invulnerable = False
        self.inicio_invuln = 0
        self.duracion_invuln = 1500

    def update(self, pressed_keys):
        # ? Mover a Jorge
        if pressed_keys[K_w]:
            self.rect.move_ip(0, -4)
        if pressed_keys[K_s]:
            self.rect.move_ip(0, 4)
        if pressed_keys[K_a]:
            self.rect.move_ip(-4, 0)
        if pressed_keys[K_d]:
            self.rect.move_ip(4, 0)

        # ? Mantener a Jorge en Pantalla
        self.rect.left = max(self.rect.left, 0)
        self.rect.right = min(self.rect.right, self.screen_width)
        self.rect.top = max(self.rect.top, 0)
        self.rect.bottom = min(self.rect.bottom, self.screen_height)

        # TODO (2.4): Actualizar las balas
        self.bullets.update()

        # Ver si terminó de ser vulnerable
        if self.invulnerable:
            if pygame.time.get_ticks() - self.inicio_invuln > self.duracion_invuln:
                self.invulnerable = False

    def shoot(self, mouse_pos):
        tiempo_actual = pygame.time.get_ticks()
        if tiempo_actual - self.ultimo_disparo > self.cooldown:
            self.ultimo_disparo = tiempo_actual

            # TODO (2.4): Calcular direccion de la bala
            distance = Vector2(mouse_pos) - Vector2(self.rect.center)
            direction = distance.normalize()

            # TODO (2.4): Crear bala y agregarla al grupo de balas
            bullet = Bullet(
            self.rect.center,
            direction,
            self.screen_width,
            self.screen_height,
            )

            self.bullets.add(bullet)
    
    def sumar_ptjs(self, puntos):
        self.ptjs += puntos

    def recibir_dano(self):
        if self.invulnerable:
            return False

        self.vidas -= 1
        self.invulnerable = True
        self.inicio_invuln = pygame.time.get_ticks()
        return self.vidas <= 0
