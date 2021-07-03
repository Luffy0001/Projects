import pygame
from random import randint


class ClownFish(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.images = []
        self.images.append(pygame.image.load("Clownfish.png"))
        self.images.append(pygame.image.load("Clownfish1.png"))

        self.index = 0

        self.rect = pygame.Rect(300, 300, 0, 0)

        self.velocity = [randint(4, 8), randint(-8, 8)]

    def update(self):
        self.index += 0

        if self.rect.x >= 650:
            self.index = 1
        if self.rect.x <= 10:
            self.index = 0

        self.image = self.images[self.index]

        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def bounce(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = randint(-8, 8)
