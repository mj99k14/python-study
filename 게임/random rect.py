import pygame
import random

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("성식이 구하기 ")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW =(255 , 255, 0)
#장애물
def create_obstacles(num_obstacles, size ,screen_width, screen_height):
    obstacles = []
    for _ in range(num_obstacles):
        while True:
            rect = pygame.Rect
                    

