import pygame
## 초기화
pygame.init()
screen = pygame.display.set_mode((800,600))


###fps적용을 위한 시간 객체 생성
clock = pygame.time.Clock()
fps = 60

##
x =screen.get_width() /2
y = screen.get_height() /2
radius = 40
speed =10 # fps 300 pixel /second

## <---메인 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    dt = clock.tick(30) /1000.0
    screen.fill((0,0,0))
    pygame.draw.circle(screen, (255,0,0),(x,y),40)
    x += speed

    if x + radius >= screen.get_width() or x - radius <=0:
        speed = -speed
    pygame.display.flip()
    ## pygame fps 설정
  
 
    clock.tick(fps)
    ##
##-->이미지생성

##게임 종료
pygame.quit()