import pygame
import pygame.draw as dr

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

White = (255, 255, 255)
Black = (0, 0, 0)
Red = (252, 33, 18)
Yellow = (245, 233, 66)

screen.fill(White)
dr.circle(screen, Yellow, (200, 200), 100, 0)
dr.circle(screen, Black, (200, 200), 100, 2)
dr.circle(screen, Red, (160, 180), 20, 0)
dr.circle(screen, Red, (240, 180), 15, 0)
dr.circle(screen, Black, (160, 180), 20, 1)
dr.circle(screen, Black, (240, 180), 15, 1)
dr.circle(screen, Black, (160, 180), 8, 0)
dr.circle(screen, Black, (240, 180), 8, 0)
dr.polygon(screen, Black, [(110, 120), (115, 113), (195, 173), (190, 180)])
dr.polygon(screen, Black, [(220, 180), (280, 120), (274, 114), (214, 174)])
dr.rect(screen, Black, (155, 250, 90, 20))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
