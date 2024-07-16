import pygame
import sys
import random


pygame.init()

screen = pygame.display.set_mode((800,600))

pygame.display.set_caption("랜덤사각형 클릭")


Blue = (0,0,255)


rect_width = 25
rect_height = 25
random_x = random.randint(0, screen.get_width() - rect_width )
random_y = random.randint(0, screen.get_height() - rect_width )
rect = pygame.Rect(random_x,random_y,rect_width,rect_height)
running =True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if rect.collidepoint(event.pos):
                random_x = random.randint(0,screen.get_width() - rect_width)
                random_y = random.randint(0,screen.get_height() - rect_height)
                rect.topleft = (random_x,random_y)

    screen.fill((255,255,255))
    pygame.draw.rect(screen,Blue,rect)
    pygame.display.flip()


pygame.quit()