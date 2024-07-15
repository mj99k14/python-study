import pygame   #1.pygame 선언

pygame.init()    #2. 초기화

screen = pygame.display.set_mode((800,600))


clock = pygame.time.Clock() # 클릭또는 움직임으로 event가 발생
running = True

while running: # 영화처럼 이어져서 나가야하기떄문에
    for event in pygame.event.get():# 이벤트확인
        if event.type == pygame.QUIT: #우측 상단의 x를 누르면 18 번 종료
            running = False
    screen.fill((0,0,0))
    pygame.display.flip()
    clock.tick(60)  #1 초당 while 60장 돈다는말 
pygame.quit()



# #4.pygame 무한루프
# def runGame():
#     global done
#     while not done:
#         clock.tick(10)
#         screen.fill(BLACK)
        
#         for event in pygame.event. get():
#             if event.type == pygame.QUIT: # [x]종료키가 누르면 게임종료
#                 done=True
                
#                 pygame.display.update()# 모든화면 그리기 업데이트

# runGame()
# pygame.quit()


# #벌레잡기 요소
# def runGame():
#     score = 0
#     start_time = int (time.time())
#     remain_time = 0
#     game_over = 0
    
#     money_image = pygame.image.load('money.png')
#     money_image = pygame.transform.scale(money_image,(60,80))
#     money =[]
#     for i in range(3):
#         money = pygame.Rect(money_image.get_rect())
#         money.left = random.randint(0,screen_width)
#         money.top = random.randint(0,screen_height)
#         dx = random.randint(-9,9)
#         dy = random.randint(-9,9)
#         money.append((money,dx,dy))
        
        
# #마우스 클릭처리 
# for (money, dx, dy) in moneys:
#     if money.collidepoint(event.pos):
#         money.remove((money, dx, dy))
        
# for event in pygame.event.get():
#     if event.type == pygame.QUIT:
#         break
#     elif event.type == pygame.MOUSEBUTTONDOWN and game_over == 0:
#         print(event.pos[0], event.pos[1])
#         for (money, dx, dy) in moneys:
#             if money.collidepoint(event.pos):
#                 print(money)
#                 moneys.remove((money, dx, dy))
#                 money = pygame.Rect(money_image.get_rect())
#                 money.left = random.randint(0, screen_width)
#                 money.top = random.randint(0, screen_height)
#                 dx = random.randint(-9, 9)
#                 dy = random.randint(-9, 9)
#                 money.append((money, dx, dy))
#                 score += 1
