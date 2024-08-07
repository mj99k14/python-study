import pygame
import random

pygame.init()
screen = pygame.display.set_mode((800,600))

screen.fill ((255,255,255))
pygame.display.flip()

# random_count = random.randint(5,20)
# print(random_count)

# random_x = random.randint(0,800)
# random_y = random.randint(0,600)
# random_c = random.randint(0,256)
# random_c1 = random.randint(0,256)
# random_c2 = random.randint(0,256)





# for _ in range(random_count):
#     pygame.draw.circle(screen, (random_c,random_c1,random_c2) ,(random_x,random_y),5)
# pygame.display.flip()

# running = True
# while running:
#      for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
# pygame.quit()

num_circles = random.randint(5,20)
for _ in range(num_circles):
    radius = random.randint(10,100)
    color =(random.randint(0,255),random.randint(0,255),random.randint(0,255))

