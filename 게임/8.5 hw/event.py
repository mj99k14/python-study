import pygame

SPAWN_ENEMY = pygame.USEREVENT + 1

pygame.time.set_timer(SPAWN_ENEMY, 2000)

for event in pygame.event.get():
    if event.type == SPAWN_ENEMY:
        print("Spwan new enemy!")

    