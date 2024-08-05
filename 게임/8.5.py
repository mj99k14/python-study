import pygame

pygame.init()

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Counter Display")
clock = pygame.time.Clock()
running = True

# 폰트 설정 (크기36)
font = pygame.font.Font(None, 36)
count = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    # 텍스트 생성 및 화면 출력
    count_text = font.render(f"count: {count}", True, (0, 0, 0))
    screen.blit(count_text, (10, 10))  # 텍스트를 화면 왼쪽 상단에 출력
    count += 1

    # 지금까지 메모리에 작성된 그림을 화면(Screen)에 출력
    pygame.display.flip()
    clock.tick(60) # clock.tick(fps number) -> 1sec/ fps number -> delta time 

pygame.quit()
