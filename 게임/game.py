import pygame   #1.pygame 선언
import random
import time

pygame.init()    #2. 초기화
#3.pygame에 사용되는 지역변수 선언
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)
large_font = pygame.font.SysFONT(None,72)
small_font = pygame.font.SysFONT(None,36)
screen_width = 400
screen_height = 600
screen = pygame.display.set_mode((screen_width,screen_height))

done = False
clock = pygame.time.clock()
#4.pygame 무한루프
def runGame():
    global done
    while not done:
        clock.tick(10)
        screen.fill(BLACK)
        
        for event in pygame.event. get():
            if event.type == pygame.QUIT: # [x]종료키가 누르면 게임종료
                done=True
                
                pygame.display.update()# 모든화면 그리기 업데이트

runGame()
pygame.quit()


#벌레잡기 요소
def runGame():
    score = 0
    start_time = int (time.time())
    remain_time = 0
    game_over = 0
    
    money_image = pygame.image.load('money.png')
    money_image = pygame.transform.scale(money_image,(60,80))
    money =[]
    for i in range(3):
        money = pygame.Rect(money_image.get_rect())
        money.left = random.randint(0,screen_width)
        money.top = random.randint(0,screen_height)
        dx = random.randint(-9,9)
        dy = random.randint(-9,9)
        money.append((money,dx,dy))
        
        
#마우스 클릭처리 
for (money, dx, dy) in moneys:
    if money.collidepoint(event.pos):
        money.remove((money, dx, dy))
        
for event in pygame.event.get():
    if event.type == pygame.QUIT:
        break
    elif event.type == pygame.MOUSEBUTTONDOWN and game_over == 0:
        print(event.pos[0], event.pos[1])
        for (money, dx, dy) in moneys:
            if money.collidepoint(event.pos):
                print(money)
                moneys.remove((money, dx, dy))
                money = pygame.Rect(money_image.get_rect())
                money.left = random.randint(0, screen_width)
                money.top = random.randint(0, screen_height)
                dx = random.randint(-9, 9)
                dy = random.randint(-9, 9)
                money.append((money, dx, dy))
                score += 1
