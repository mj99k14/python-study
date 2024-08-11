import pygame
import random
#pygame 초기화
pygame.init()
#화면 설정
screen_width,screen_height = 800, 600
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Falling squares Example')
# 색상정의
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
#사각형 크기와 속도 설정
square_size = 50
falling_speed = 200

#사각형 리스트
falling_squares = []

#사용자 정의 이벤트 설정
SPAWN_SQUARE = pygame.USEREVENT +1
pygame.time.set_timer(SPAWN_SQUARE, 1000)
#fps 제어를 위한 clock 객체 생성
clock = pygame.time.Clock()

def spawn_square():
    # 랜덤한 x위치 에 새로운 사각형 생성
    x_position = random.randint(0 , screen_width - square_size)
    new_square = pygame.Rect(x_position, 0 ,square_size ,square_size)
    falling_squares.append(new_square)
#게임 루프
running = True
while running:
    #델타 타임 계산
    dt = clock.tick(60) / 1000.0
    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running =False

        elif event.type == SPAWN_SQUARE:
            spawn_square() #사각형 생성 이벤트 발생시 사각형 추가

    for square in falling_squares[:]:
        square.y += falling_speed * dt # 델타 타임을 사용한 이동
        if square.top > screen_height: 
            falling_squares.remove(square) # 화면을 벗아나면 제거
    #화면 초기화
    screen.fill(WHITE)
    #사각형 그리기
    for square in falling_squares:
        pygame.draw.rect(screen,BLUE,square)
    #화면 업데이트
    pygame.display.flip()
#게임 종료
pygame.quit