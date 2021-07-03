import pygame
from random import randint


class Fish(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.images = []
        self.images.append(pygame.image.load('Jellyfish1.png'))
        self.images.append(pygame.image.load('Jellyfish3.png'))
        self.images.append(pygame.image.load('Jellyfish4.png'))
        self.images.append(pygame.image.load('Jellyfish5.png'))
        self.images.append(pygame.image.load('Jellyfish6.png'))

        self.index = 0

        self.image = self.images[self.index]

        self.rect = pygame.Rect(50, 50, 0, 0)

        self.velocity = [randint(4, 8), randint(-8, 8)]

    def update(self):
        self.index += 1

        if self.index >= len(self.images):
            self.index = 0

        self.image = self.images[self.index]

        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def bounce(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = randint(-8, 8)
