import pygame
import random

pygame.init()

screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('성식이 먹이주기 게임')

WHITE = (255, 255, 255)
BLUE =(0, 0, 255)
RED = (255, 0 ,0)
GREEN = (0, 255 ,0)
YELLOW = (255, 255 , 0)

def create_obstacles(num_obstacles, size , screen_width, screen_height):

    obstacles = []

    for _ in range(num_obstacles):
        while True:
            rect = pygame.Rect(random.randint(0, screen_width - size),\
                               random.randint(0, screen_height - size), size, size)
            if not any(rect.colliderect(o) for o in obstacles):
                obstacles.append(rect)
                break
    return obstacles

def create_items(num_items, size , screen_width, screen_height, obstacles):

    items = []

    for _ in range(num_items):
        while True:
            rect = pygame.Rect(random.randint(0, screen_width - size),\
                                random.randint(0, screen_height - size),size, size)
            if not any(rect.colliderect(o) for o in obstacles) and \
                not any(rect.colliderect(i) for i in items):
                items.append(rect)
                break
    return items

obstacles = create_obstacles(5, 50 , screen_width, screen_height)
items = create_items(10, 20 , screen_width, screen_height ,obstacles)
moster = pygame.image.load("kkk.png")
moster_rect = moster.get_rect()
moster_rect_width = moster_rect.width
moster_rect_height = moster_rect.height
moster_rect.x = moster_rect.y 
moster_rect.y = moster_rect.x
while True:
    random_x = random.randint(0, screen_width - moster_rect_width)
    random_y = random.randint(0, screen_height - moster_rect_height)
    temp_rect = pygame.Rect(random_x, random_y, moster_rect_width, moster_rect_height)
    if temp_rect.collidelist(obstacles) == -1 and temp_rect.collidelist(items) == -1:
        moster_rect.topleft = (random_x, random_y)
        break


velocity = 300
clock = pygame.time.Clock()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    previous_position = moster_rect.topleft

    dt = clock.tick(60)/1000.0

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        moster_rect.x -= velocity * dt
    if keys[pygame.K_RIGHT]:
        moster_rect.x += velocity * dt
    if keys[pygame.K_UP]:
        moster_rect.y -= velocity * dt
    if keys[pygame.K_DOWN]:
        moster_rect.y += velocity * dt

    collision_index = moster_rect.collidelist(obstacles)
    if collision_index != -1:
        print(f"장애물 {collision_index}와 충돌 ! 성식이 아픔!.병원감  ")
        moster_rect.topleft = previous_position
        screen.fill(BLUE)
        pygame.display.flip()
        running = False
        running = False
    item_index = moster_rect.collidelist(items)
    if item_index != -1:
        print(f"성식이 먹이 나머지:{len(items)-1}")
        del items[item_index]
       
    if not items:
        print("모든 아이템을 수집했습니다! 성식이 다 먹음!") 
        running = False

    screen.fill(WHITE)

    for obs in obstacles:
        pygame.draw.rect(screen, BLUE, obs)

    for item in items:
        pygame.draw.rect(screen ,YELLOW, item)
    
    screen.blit(moster,moster_rect)
    

    pygame.display.flip()


pygame.quit()