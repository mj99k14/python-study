import pygame

pygame.init()


sound_fire = pygame.mixer.Sound("fire.mp3")

sound_fire.set_volume(0.5)

screen = pygame.display.set_mode((640, 480))
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                sound_fire.play()
                print("총 소리 재생 ") 