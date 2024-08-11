import pygame
import random

pygame.init()

screen_width,screen_height = 800, 600
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Collect Items Game")
clock = pygame.time.Clock()
velocity = 300
running =True
#장애물 사이즈
obs_width= 200
obs_height = 150
num = 5
#아이템
item_width = 50
item_height = 50

moving_width = 60
moving_height = 60

#만들고싶은 랜덤 좌표
obs_list = []

for obs in range(num):
    while True:
        obstacles_x = random.randint(0 , screen_width - obs_width )
        obstacles_y = random.randint(0 , screen_height - obs_height )
        obs_rect= pygame.Rect (obstacles_x, obstacles_y, obs_width, obs_height)
        # 장애물이 장애물들이랑  부딪히지않으면 
        if obs_rect.collidelist(obs_list) == -1:
    #새로운 리스트레에저장하고 반복문  종료
            obs_list.append(obs_rect)
            break 

item_list = []

for item in range(num):
    while True:
        item_x = random.randint(0 , screen_width - item_width)
        item_y = random.randint(0, screen_height - item_height)
        item_rect = pygame.Rect(item_x,item_y,item_width,item_height)
        # 아이템이 아이템이랑 겹치지않아하고 아이템이 장애물이랑 겹치면 ㄴㄴ
        if item_rect.collidelist(item_list)== -1 and \
            item_rect.collidelist(obs_list) == -1:
            item_list.append(item_rect)
            break

while True:
    moving_x = random.randint( 0 , screen_width - moving_width)
    moving_y = random.randint(0, screen_height - moving_height)
    moving_rect = pygame.Rect(moving_x,moving_y,moving_width,moving_height)
    # 장애물이랑 아이템 이랑 충돌되지않게 위치
    if moving_rect.collidelist(obs_list) ==-1 and\
            moving_rect.collidelist(item_list) == -1:
            break

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    previous_postion = moving_rect.topleft

    dt = clock.tick(60) / 1000.0

    keys =pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        moving_rect.x -= velocity * dt
    if keys[pygame.K_RIGHT]:
        moving_rect.x += velocity * dt
    if keys[pygame.K_UP]:
        moving_rect.y  -= velocity * dt
    if keys[pygame.K_DOWN]:
        moving_rect.y  += velocity * dt
    #화면경계처리
    moving_rect.x = max(0, min(moving_rect.x, screen_width - moving_width))
    moving_rect.y = max(0, min(moving_rect.y, screen_height - moving_height))

    #충돌감지 
    if moving_rect.collidelist(obs_list) != -1:
        moving_rect.topleft = previous_postion
    
    col = moving_rect.collidelist(item_list) 
    if col != -1:
        del item_list[col]
   
    screen.fill((255,255,255))
    #장애물 그리기
    for obs in obs_list:
        pygame.draw.rect(screen,(255, 0 , 0) , obs)
    
    #아이템 그리기
    for item in item_list:
        pygame.draw.rect(screen,(0, 255, 0) ,item)
     
    #아이템 리스트에 아무것도 없으면 종료
 
    if not item_list:
        running = False

    #움직이는 사각형
    pygame.draw.rect(screen, (0, 0, 255), moving_rect)
    
    pygame.display.flip()

pygame.quit()