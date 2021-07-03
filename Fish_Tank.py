import pygame
from fish import Fish
from fish2 import Fish2
from purplefish import PurpleFish
from fish4 import Fish4
from clownfish import ClownFish

size = (700, 500)
pygame.display.set_caption("Fish Tank")
background = pygame.image.load("Background.png")


def fish_tank():
    pygame.init()
    screen = pygame.display.set_mode(size)
    fish = Fish()
    fish2 = Fish2()
    fish3 = PurpleFish()
    fish4 = Fish4()
    clownfish = ClownFish()
    all_sprites_list = pygame.sprite.Group()
    all_sprites_list.add(fish)
    all_sprites_list.add(fish2)
    all_sprites_list.add(fish3)
    all_sprites_list.add(fish4)
    all_sprites_list.add(clownfish)
    clock = pygame.time.Clock()

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        all_sprites_list.update()
        screen.blit(background, [0, 0])
        all_sprites_list.draw(screen)
        pygame.display.update()

        if fish.rect.x >= 655:
            fish.velocity[0] = -fish.velocity[0]
        if fish.rect.x <= 20:
            fish.velocity[0] = -fish.velocity[0]
        if fish.rect.y > 380:
            fish.velocity[1] = -fish.velocity[1]
        if fish.rect.y < 15:
            fish.velocity[1] = -fish.velocity[1]

        if fish2.rect.x >= 620:
            fish2.velocity[0] = -fish2.velocity[0]
        if fish2.rect.x <= 10:
            fish2.velocity[0] = -fish2.velocity[0]
        if fish2.rect.y > 365:
            fish2.velocity[1] = -fish2.velocity[1]
        if fish2.rect.y < 15:
            fish2.velocity[1] = -fish2.velocity[1]

        if fish3.rect.x >= 620:
            fish3.velocity[0] = -fish3.velocity[0]
        if fish3.rect.x <= 10:
            fish3.velocity[0] = -fish3.velocity[0]
        if fish3.rect.y > 365:
            fish3.velocity[1] = -fish3.velocity[1]
        if fish3.rect.y < 15:
            fish3.velocity[1] = -fish3.velocity[1]

        if fish4.rect.x >= 650:
            fish4.velocity[0] = -fish4.velocity[0]
        if fish4.rect.x <= 10:
            fish4.velocity[0] = -fish4.velocity[0]
        if fish4.rect.y > 365:
            fish4.velocity[1] = -fish4.velocity[1]
        if fish4.rect.y < 15:
            fish4.velocity[1] = -fish4.velocity[1]

        if clownfish.rect.x >= 650:
            clownfish.velocity[0] = -clownfish.velocity[0]
        if clownfish.rect.x <= 10:
            clownfish.velocity[0] = -clownfish.velocity[0]
        if clownfish.rect.y > 365:
            clownfish.velocity[1] = -clownfish.velocity[1]
        if clownfish.rect.y < 15:
            clownfish.velocity[1] = -clownfish.velocity[1]
        # pygame.display.flip()
        clock.tick(10)

    pygame.quit()


if __name__ == '__main__':
    fish_tank()
