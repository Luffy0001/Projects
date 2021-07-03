import pygame
from random import randint


class Fish2(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.images = []
        self.images.append(pygame.image.load("Guppy Large Normal.png"))
        self.images.append(pygame.image.load("Guppy Large fliped.png"))

        self.index = 0

        self.rect = pygame.Rect(100, 100, 0, 0)

        self.velocity = [randint(4, 8), randint(-8, 8)]

    def update(self):
        self.index += 0

        if self.rect.x >= 620:
            self.index = 1
        if self.rect.x <= 10:
            self.index = 0

        self.image = self.images[self.index]

        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def bounce(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = randint(-8, 8)
