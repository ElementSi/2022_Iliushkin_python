import pygame
import pygame.draw as dr

pygame.init()

FPS = 30
screen = pygame.display.set_mode((600, 800))

# Creating palette
Black = (0, 0, 0)
MoonGray = (240, 240, 240)
SkyGray = (130, 130, 130)
Cloud1Gray = (103, 103, 103)
Cloud2Gray = (65, 65, 65)
Cloud3Gray = (35, 35, 35)
RoofGray = (21, 21, 21)
BalconyGray = (40, 40, 40)
GhostGray = (210, 210, 210)
ChimneyGray = (42, 42, 42)
BuildingBrown = (69, 56, 12)
BuildingBeige = (84, 74, 69)
WindowBrown = (59, 29, 7)
WindowYellow = (240, 196, 53)
GhostBlue = (108, 211, 240)

# Drawing background
screen.fill(Black)
dr.rect(screen, SkyGray, (0, 0, 600, 330))
dr.circle(screen, MoonGray, (540, 70), 50, 0)
dr.ellipse(screen, Cloud3Gray, (300, 200, 500, 50), 0)

# Drawing building
dr.rect(screen, BuildingBrown, (40, 175, 310, 400))
dr.polygon(screen, RoofGray, [(5, 175), (50, 135), (320, 135), (385, 175)], 0)

# Drawing clouds and chimneys
dr.rect(screen, ChimneyGray, (85, 105, 10, 50))
dr.rect(screen, ChimneyGray, (225, 85, 8, 50))
dr.ellipse(screen, Cloud2Gray, (25, 65, 450, 60), 0)
dr.ellipse(screen, Cloud1Gray, (260, 35, 350, 60), 0)
dr.ellipse(screen, Cloud1Gray, (370, 115, 450, 45), 0)
dr.rect(screen, ChimneyGray, (100, 85, 18, 75))
dr.rect(screen, ChimneyGray, (295, 100, 11, 60))

# Drawing building details
dr.rect(screen, BuildingBeige, (60, 176, 35, 150))
dr.rect(screen, BuildingBeige, (120, 176, 35, 150))
dr.rect(screen, BuildingBeige, (200, 176, 35, 150))
dr.rect(screen, BuildingBeige, (280, 176, 35, 150))

# Drawing balcony
dr.rect(screen, BalconyGray, (5, 340, 380, 40))
for i in range(10, 380, 60):
    dr.rect(screen, BalconyGray, (i, 300, 10, 40))
dr.rect(screen, BalconyGray, (20, 280, 350, 20))

# Drawing windows
dr.rect(screen, WindowBrown, (80, 460, 60, 70))
dr.rect(screen, WindowBrown, (165, 460, 60, 70))
dr.rect(screen, WindowYellow, (250, 460, 60, 70))

# Drawing ghost body
dr.circle(screen, GhostGray, (475, 600), 25, 0)
dr.circle(screen, GhostGray, (410, 700), 5, 0)
dr.circle(screen, GhostGray, (470, 710), 18, 0)
dr.circle(screen, GhostGray, (530, 690), 30, 0)
dr.circle(screen, GhostGray, (565, 650), 20, 0)
dr.circle(screen, GhostGray, (500, 615), 20, 0)
dr.polygon(screen, GhostGray,
           [(450, 600), (447, 630), (427, 654), (420, 682), (406, 698), (414, 702), (436, 694), (455, 705),
            (455, 700), (485, 716), (520, 700), (550, 680), (566, 664), (574, 641), (512, 600), (450, 600)], 0)
dr.circle(screen, Black, (400, 612), 51, 0)
dr.circle(screen, Black, (400, 650), 30, 0)
dr.circle(screen, Black, (443, 710), 17, 0)
dr.circle(screen, Black, (445, 725), 17, 0)
dr.circle(screen, Black, (445, 725), 17, 0)
dr.circle(screen, Black, (502, 714), 17, 0)
dr.circle(screen, Black, (565, 680), 14, 0)
dr.circle(screen, Black, (520, 745), 35, 0)
dr.circle(screen, Black, (573, 563), 70, 0)
dr.circle(screen, GhostGray, (509, 674), 36, 0)
dr.circle(screen, GhostGray, (484, 698), 20, 0)
dr.circle(screen, GhostGray, (521, 645), 35, 0)
dr.circle(screen, Black, (574, 695), 21, 0)

# Drawing ghost eyes
dr.circle(screen, GhostBlue, (464, 596), 6, 0)
dr.circle(screen, GhostBlue, (484, 592), 6, 0)
dr.circle(screen, Black, (462, 596), 2, 0)
dr.circle(screen, Black, (482, 592), 2, 0)
dr.polygon(screen, MoonGray, [(463, 595), (468, 592), (469, 594), (466, 595), (463, 595)], 0)
dr.polygon(screen, MoonGray, [(483, 591), (488, 588), (488, 590), (488, 591), (483, 591)], 0)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
