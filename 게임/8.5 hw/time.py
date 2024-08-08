import pygame

pygame.init()

screen_width, screen_height = 800, 600
screen =  pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Timer Display Example')

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

font = pygame.font.Font(None, 36)

start_time = pygame.time.get_ticks()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running =False

    elapsed_time = (pygame.time.get_ticks() - start_time) /1000
    
    screen.fill(WHITE)

    timer_text = font.render(f"Time: {elapsed_time:.2f} seconds", True, BLACK)

    screen.blit(timer_text,(10,10))

    pygame.display.flip()

pygame.quit()