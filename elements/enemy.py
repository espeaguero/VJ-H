if __name__ == "__main__":
    raise RuntimeError(
        "\033c❌ ESTE ARCHIVO NO DEBE EJECUTARSE. EJECUTA main.py"
    )

import random

import pygame

BUGpng = pygame.image.load("assets/bug.png")
BUGpng_scaled = pygame.transform.scale(BUGpng, (64, 64))

ABEJApng = pygame.image.load("assets/abeja.png")
ABEJApng_scaled = pygame.transform.scale(ABEJApng, (80, 60))

RANApng = pygame.image.load("assets/rana.png")
RANApng_scaled = pygame.transform.scale(RANApng, (70, 70))


class Enemy(pygame.sprite.Sprite):
    def __init__(self, screen):
        super().__init__()

        self.image = BUGpng_scaled
        self.rect = self.image.get_rect(
            center=(
                screen.get_width() + 100,
                random.randint(0, screen.get_height()),
            )
        )
        self.speed = random.randint(3, 5)

    def update(self):
        # Mover a los enemigos
        self.rect.move_ip(-self.speed, 0)

        # Destruir a los enemigos
        if self.rect.right < 0:
            self.kill()


class Abeja(pygame.sprite.Sprite):
    def __init__(self, screen):
        super().__init__()

        self.image = ABEJApng_scaled
        self.rect = self.image.get_rect(
            center=(
                screen.get_width() + 100,
                random.randint(50, screen.get_height() - 50),
            )
        )
        self.speed = 5
        self.speed_vertical = 3
        self.pasos = 0
        self.screen_height = screen.get_height()

    def update(self):
        self.rect.move_ip(-self.speed, self.speed_vertical)
        self.pasos += 1

        if (
            self.pasos >= 30
            or self.rect.top <= 0
            or self.rect.bottom >= self.screen_height
        ):
            self.speed_vertical *= -1
            self.pasos = 0

        if self.rect.right < 0:
            self.kill()


class Rana(pygame.sprite.Sprite):
    def __init__(self, screen):
        super().__init__()

        self.image = RANApng_scaled
        self.rect = self.image.get_rect(
            center=(
                screen.get_width() + 100,
                random.randint(100, screen.get_height() - 50),
            )
        )
        self.speed = 8
        self.pasos = 0

    def update(self):
        self.pasos += 1

        if self.pasos <= 10:
            self.rect.move_ip(-self.speed, -4)

        elif self.pasos <= 20:
            self.rect.move_ip(-self.speed, 4)

        elif self.pasos >= 60:
            self.pasos = 0

        if self.rect.right < 0:
            self.kill()