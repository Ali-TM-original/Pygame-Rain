import pygame
import random
import sys

clock = pygame.time.Clock()

screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Rain')
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

rain_drop_list = []
for i in range(60):
    x_of_rain = random.randrange(0, 600)
    y_of_rain = random.randrange(0, 600)
    rain_drop_list.append([x_of_rain, y_of_rain])

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(BLACK)
    for item in rain_drop_list:
        item[1] += 1
        pygame.draw.circle(screen, WHITE, item, 2)
        if item[1] >= 600:
            item[1] = 0

    pygame.display.update()
    clock.tick(60)
