import pygame
import os


# 현재 파일이 있는 디렉토리 경로를 가져옵니다.
current_directory = os.path.dirname(os.path.abspath(__file__))

# 파일 이름을 지정합니다.
filename = "background.mp3"

# 파일의 전체 경로를 만듭니다.
file_path = os.path.join(current_directory, filename)


pygame.init()

background_music = pygame.mixer.music.load(file_path)

pygame.mixer.music.play(-1) # 음악 무한반복

screen = pygame.display.set_mode((640, 480))

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running == False
            
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                pygame.mixer.music.stop()
                print("음악 정지")
            elif event.key == pygame.K_p:
                pygame.mixer.music.play()
                print("음악 재생")
            elif event.key == pygame.K_i:
                pygame.mixer.music.play(fade_ms= 3000)
                print("음악 재생 - fade-in mode")
            elif event.key == pygame.K_o:
                pygame.mixer.music.fadeout(3000)
                print("음악 종료 -fade - out mode")
            elif event.key == pygame.K_u:
                current_vol = pygame.mixer.music.get_volume()
                current_vol += 0.1
                pygame.mixer.music.set_volume(current_vol)
                print(f"볼륨 증가:{current_vol}")
            elif event.key == pygame.K_d:
                current_vol = pygame.mixer.music.get_volume()
                current_vol = max(0.0, current_vol - 0.1)
                pygame.mixer.music.set_volume(current_vol)
                print(f"볼륨 감소: {current_vol}")

pygame.quit()