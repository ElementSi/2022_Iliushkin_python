import pygame
import pygame.draw as dr

pygame.init()

FPS = 30
screen = pygame.display.set_mode((600, 800))

Black = (0, 0, 0)
MoonGray = (240, 240, 240)
SkyGray = (130, 130, 130)
Cloud1Gray = (103, 103, 103)
Cloud2Gray = (65, 65, 65)
Cloud3Gray = (35, 35, 35)
RoofGray = (21, 21, 21)
BalconyGray = (40, 40, 40)
GhostGray = (210, 210, 210)
PipeGray = (42, 42, 42)
BuildingBrown = (69, 56, 12)
BuildingBeige = (84, 74, 69)
WindowBrown = (59, 29, 7)
WindowYellow = (240, 196, 53)

screen.fill(Black)
dr.rect(screen, SkyGray, (0, 0, 600, 330))
dr.circle(screen, MoonGray, (540, 70), 50, 0)
dr.ellipse(screen, Cloud3Gray, (300, 200, 500, 50), 0)

dr.rect(screen, BuildingBrown, (40, 175, 310, 400))
dr.polygon(screen, RoofGray, [(5, 175), (50, 135), (320, 135), (385, 175)], 0)

dr.rect(screen, PipeGray, (85, 105, 10, 50))
dr.rect(screen, PipeGray, (225, 85, 8, 50))
dr.ellipse(screen, Cloud2Gray, (25, 65, 450, 60), 0)
dr.ellipse(screen, Cloud1Gray, (260, 35, 350, 60), 0)
dr.ellipse(screen, Cloud1Gray, (370, 115, 450, 45), 0)
dr.rect(screen, PipeGray, (100, 85, 18, 75))
dr.rect(screen, PipeGray, (295, 100, 11, 60))

dr.rect(screen, BuildingBeige, (60, 176, 35, 150))
dr.rect(screen, BuildingBeige, (120, 176, 35, 150))
dr.rect(screen, BuildingBeige, (200, 176, 35, 150))
dr.rect(screen, BuildingBeige, (280, 176, 35, 150))

dr.rect(screen, BalconyGray, (5, 340, 380, 40))
for i in range(10, 380, 60):
    dr.rect(screen, BalconyGray, (i, 300, 10, 40))
dr.rect(screen, BalconyGray, (20, 280, 350, 20))

dr.rect(screen, WindowBrown, (80, 460, 60, 70))
dr.rect(screen, WindowBrown, (165, 460, 60, 70))
dr.rect(screen, WindowYellow, (250, 460, 60, 70))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
