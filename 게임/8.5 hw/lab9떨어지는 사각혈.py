import pygame
import random

pygame.init()

screen_width,screen_height = 800, 600
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Falling Squares Example')

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

squares_size = 50
falling_speed = 200

falling_squares = []

SPAWN_SQUARE =pygame.USEREVENT + 1
pygame.time.set_timer(SPAWN_SQUARE ,1000)

clock = pygame.time.Clock()

def spawn_square():
    x_position = random.randint(0, screen_width - squares_size)
    new_square = pygame.Rect(x_position ,0, squares_size, squares_size)
    falling_squares.append(new_square)

running = True
while running:

    dt = clock.tick(60) /1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running =False

        elif event.type == SPAWN_SQUARE:
            spawn_square()

    for square in falling_squares[:]:
        square.y += falling_speed * dt
        if square.top > screen_height:
            falling_squares.remove(square)

    screen.fill(WHITE)

    for square in falling_squares:
        pygame.draw.rect(screen,BLUE,square)

    pygame.display.flip()

pygame.quit()