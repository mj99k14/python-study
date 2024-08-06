import pygame

pygame.init()

screen_width,screen_height = 800, 600
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Collidelist Example")

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

obstacles = [
    pygame.Rect(150, 100, 100, 100),
    pygame.Rect(300, 300, 150, 50),
    pygame.Rect(500, 200, 50, 150),
    pygame.Rect(400, 400, 200, 50)
]

moving_rect =  pygame.Rect(50, 50, 50, 50)

velocity = 300
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    previous_position = moving_rect.topleft

    dt = clock.tick(60)/ 1000.0

    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        moving_rect.x -= velocity * dt
    if keys[pygame.K_RIGHT]:
        moving_rect.x += velocity * dt
    if keys[pygame.K_UP]:
        moving_rect.y -= velocity * dt
    if keys[pygame.K_DOWN]:
        moving_rect.y += velocity * dt

    collision_index = moving_rect.collidelist(obstacles)
    if collision_index != -1:
        print(f"Collision with obstacle {collision_index}")
        moving_rect.topleft = previous_position


    screen.fill(WHITE)

    for obs in obstacles:
        pygame.draw.rect(screen, BLUE, obs)

    pygame.draw.rect(screen, RED, moving_rect)

    pygame.display.flip()

pygame.quit()