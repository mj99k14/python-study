import pygame
pygame.init()
screen  =pygame.display.set_mode((800,600))
pygame.display.set_caption("연습입네다~!")

speed = 5
x,y =400,300

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running =False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -=speed
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed

    screen.fill((255,255,255))

    pygame.draw.rect(screen,(0,0,0),(x,y,50,50)) #화면,색깔,x,y축 ,사각형 그리기

    pygame.display.flip()

    clock.tick(60)

pygame.quit()      