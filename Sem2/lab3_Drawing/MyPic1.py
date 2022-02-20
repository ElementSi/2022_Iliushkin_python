import pygame
import pygame.draw as dr

pygame.init()

FPS = 30
Screen = pygame.display.set_mode((600, 800))

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
Screen.fill(Black)
dr.rect(Screen, SkyGray, (0, 0, 600, 330))
dr.circle(Screen, MoonGray, (540, 70), 50, 0)
dr.ellipse(Screen, Cloud3Gray, (300, 200, 500, 50), 0)

# Drawing building
dr.rect(Screen, BuildingBrown, (40, 175, 310, 400))
dr.polygon(Screen, RoofGray, [(5, 175), (50, 135), (320, 135), (385, 175)], 0)

# Drawing clouds and chimneys
dr.rect(Screen, ChimneyGray, (85, 105, 10, 50))
dr.rect(Screen, ChimneyGray, (225, 85, 8, 50))
dr.ellipse(Screen, Cloud2Gray, (25, 65, 450, 60), 0)
dr.ellipse(Screen, Cloud1Gray, (260, 35, 350, 60), 0)
dr.ellipse(Screen, Cloud1Gray, (370, 115, 450, 45), 0)
dr.rect(Screen, ChimneyGray, (100, 85, 18, 75))
dr.rect(Screen, ChimneyGray, (295, 100, 11, 60))

# Drawing building details
dr.rect(Screen, BuildingBeige, (60, 176, 35, 150))
dr.rect(Screen, BuildingBeige, (120, 176, 35, 150))
dr.rect(Screen, BuildingBeige, (200, 176, 35, 150))
dr.rect(Screen, BuildingBeige, (280, 176, 35, 150))

# Drawing balcony
dr.rect(Screen, BalconyGray, (5, 340, 380, 40))
for i in range(10, 380, 60):
    dr.rect(Screen, BalconyGray, (i, 300, 10, 40))
dr.rect(Screen, BalconyGray, (20, 280, 350, 20))

# Drawing windows
dr.rect(Screen, WindowBrown, (80, 460, 60, 70))
dr.rect(Screen, WindowBrown, (165, 460, 60, 70))
dr.rect(Screen, WindowYellow, (250, 460, 60, 70))

# Drawing ghost body
dr.circle(Screen, GhostGray, (475, 600), 25, 0)
dr.circle(Screen, GhostGray, (410, 700), 5, 0)
dr.circle(Screen, GhostGray, (470, 710), 18, 0)
dr.circle(Screen, GhostGray, (530, 690), 30, 0)
dr.circle(Screen, GhostGray, (565, 650), 20, 0)
dr.circle(Screen, GhostGray, (500, 615), 20, 0)
dr.polygon(Screen, GhostGray,
           [(450, 600), (447, 630), (427, 654), (420, 682), (406, 698), (414, 702), (436, 694), (455, 705),
            (455, 700), (485, 716), (520, 700), (550, 680), (566, 664), (574, 641), (512, 600), (450, 600)], 0)
dr.circle(Screen, Black, (400, 612), 51, 0)
dr.circle(Screen, Black, (400, 650), 30, 0)
dr.circle(Screen, Black, (443, 710), 17, 0)
dr.circle(Screen, Black, (445, 725), 17, 0)
dr.circle(Screen, Black, (502, 714), 17, 0)
dr.circle(Screen, Black, (565, 680), 14, 0)
dr.circle(Screen, Black, (520, 745), 35, 0)
dr.circle(Screen, GhostGray, (509, 674), 36, 0)
dr.circle(Screen, GhostGray, (484, 698), 20, 0)
dr.circle(Screen, GhostGray, (521, 645), 35, 0)
dr.circle(Screen, Black, (574, 695), 21, 0)
dr.circle(Screen, Black, (542, 587), 32, 0)
dr.circle(Screen, Black, (555, 597), 32, 0)

# Drawing ghost eyes
dr.circle(Screen, GhostBlue, (464, 596), 6, 0)
dr.circle(Screen, GhostBlue, (484, 592), 6, 0)
dr.circle(Screen, Black, (462, 596), 2, 0)
dr.circle(Screen, Black, (482, 592), 2, 0)
dr.polygon(Screen, MoonGray, [(463, 595), (468, 592), (469, 594), (466, 595), (463, 595)], 0)
dr.polygon(Screen, MoonGray, [(483, 591), (488, 588), (488, 590), (488, 591), (483, 591)], 0)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
