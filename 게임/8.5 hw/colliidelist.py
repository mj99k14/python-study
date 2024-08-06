#collidelist은 충돌하는지않하는지확인하는 메소드
#어떤 사각형과도 충돌하지 않는 경우 -1

import pygame

pygame.init()

rects = [
    pygame.Rect(20, 20, 40, 40),
    pygame.Rect(100,100,50,50),
    pygame.Rect(200,200,60,60)
]

moving_rect = pygame.Rect(120, 130, 100, 100)

index = moving_rect.collidelist(rects)

if index != -1:
    print(f"movin_rect가 rects [{index}]와 충돌했습니다. ")
else:
    print("충돌이 없습니다. ")