import pygame   #1.pygame 선언

pygame.init()    #2. 초기화
#화면 가로 ,세로 크기 출력
screen = pygame.display.set_mode((800, 600))
#색상 정의
WHITE = (255, 255, 255)
RED = (255, 0, 0)

#화면 지우기 
screen.fill(WHITE)

#점 그리기
pygame.draw.circle(screen, RED ,(0,0),5)
pygame.draw.circle(screen, RED ,(799, 0), 5)
pygame.draw.circle(screen, RED ,(0, 599), 5)
pygame.draw.circle(screen, RED ,(799, 599), 5)

#대각선 그리기
pygame.draw.line(screen, RED ,(0, 0), (799,599))
pygame.draw.line(screen, RED ,(799, 0), (0,599))

pygame.display.flip() # 메모리에 저장해놧다가 한번에 실제 화면에 보여주기 위해서
running =True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
