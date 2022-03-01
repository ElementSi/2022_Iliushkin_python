import pygame
import pygame.draw as dr

pygame.init()

FPS = 30
Screen = pygame.display.set_mode((600, 800))
TransparentScreen1 = pygame.Surface((600, 800), pygame.SRCALPHA)
TransparentScreen2 = pygame.Surface((600, 800), pygame.SRCALPHA)
TransparentScreen3 = pygame.Surface((600, 800), pygame.SRCALPHA)


def affinity(x, y, kx, ky, dx, dy):
    x = x * kx + dx
    y = y * ky + dy
    return [x, y]


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

# Drawing buildings
bComp = 0.45
bShiftX = (430, 180, 0)
bShiftY = (130, 230, 300)
bAlpha = (128, 200, 255)
for i in range(0, 2):
    # Drawing building
    dr.rect(TransparentScreen1, BuildingBrown + (bAlpha[i],),
            (40 * bComp + bShiftX[i], 175 * bComp + bShiftY[i], 310 * bComp, 400 * bComp))
    dr.rect(TransparentScreen1, BuildingBeige + (bAlpha[i],),
            (60 * bComp + bShiftX[i], 176 * bComp + bShiftY[i], 35 * bComp, 150 * bComp))
    dr.rect(TransparentScreen1, BuildingBeige + (bAlpha[i],),
            (120 * bComp + bShiftX[i], 176 * bComp + bShiftY[i], 35 * bComp, 150 * bComp))
    dr.rect(TransparentScreen1, BuildingBeige + (bAlpha[i],),
            (200 * bComp + bShiftX[i], 176 * bComp + bShiftY[i], 35 * bComp, 150 * bComp))
    dr.rect(TransparentScreen1, BuildingBeige + (bAlpha[i],),
            (280 * bComp + bShiftX[i], 176 * bComp + bShiftY[i], 35 * bComp, 150 * bComp))
    dr.polygon(TransparentScreen1, RoofGray + (bAlpha[i],),
               [affinity(5, 175, bComp, bComp, bShiftX[i], bShiftY[i]),
                affinity(50, 135, bComp, bComp, bShiftX[i], bShiftY[i]),
                affinity(320, 135, bComp, bComp, bShiftX[i], bShiftY[i]),
                affinity(385, 175, bComp, bComp, bShiftX[i], bShiftY[i])], 0)

    # Drawing chimneys
    dr.rect(TransparentScreen1, ChimneyGray + (bAlpha[i],),
            (85 * bComp + bShiftX[i], 105 * bComp + bShiftY[i], 10 * bComp, 50 * bComp))
    dr.rect(TransparentScreen1, ChimneyGray + (bAlpha[i],),
            (225 * bComp + bShiftX[i], 85 * bComp + bShiftY[i], 8 * bComp, 50 * bComp))
    dr.rect(TransparentScreen1, ChimneyGray + (bAlpha[i],),
            (100 * bComp + bShiftX[i], 85 * bComp + bShiftY[i], 18 * bComp, 75 * bComp))
    dr.rect(TransparentScreen1, ChimneyGray + (bAlpha[i],),
            (295 * bComp + bShiftX[i], 100 * bComp + bShiftY[i], 11 * bComp, 60 * bComp))

    # Drawing balcony
    dr.rect(TransparentScreen1, BalconyGray + (bAlpha[i],),
            (5 * bComp + bShiftX[i], 340 * bComp + bShiftY[i], 380 * bComp, 40 * bComp))
    for j in range(10, 380, 60):
        dr.rect(TransparentScreen1, BalconyGray + (bAlpha[i],),
                (j * bComp + bShiftX[i], 300 * bComp + bShiftY[i], 10 * bComp, 40 * bComp))
    dr.rect(TransparentScreen1, BalconyGray + (bAlpha[i],),
            (20 * bComp + bShiftX[i], 280 * bComp + bShiftY[i], 350 * bComp, 20 * bComp))

    # Drawing windows
    dr.rect(TransparentScreen1, WindowBrown + (bAlpha[i],),
            (80 * bComp + bShiftX[i], 460 * bComp + bShiftY[i], 60 * bComp, 70 * bComp))
    dr.rect(TransparentScreen1, WindowBrown + (bAlpha[i],),
            (165 * bComp + bShiftX[i], 460 * bComp + bShiftY[i], 60 * bComp, 70 * bComp))
    dr.rect(TransparentScreen1, WindowYellow + (bAlpha[i],),
            (250 * bComp + bShiftX[i], 460 * bComp + bShiftY[i], 60 * bComp, 70 * bComp))

    # Drawing special in building clouds
    dr.ellipse(TransparentScreen2, Cloud2Gray + (200,), (-65, 430, 350, 40))
    dr.ellipse(TransparentScreen2, Cloud2Gray + (200,), (260, 380, 400, 45))

# Drawing one more building
dr.rect(TransparentScreen3, BuildingBrown + (bAlpha[2],),
        (40 * bComp + bShiftX[2], 175 * bComp + bShiftY[2], 310 * bComp, 400 * bComp))
dr.rect(TransparentScreen3, BuildingBeige + (bAlpha[2],),
        (60 * bComp + bShiftX[2], 176 * bComp + bShiftY[2], 35 * bComp, 150 * bComp))
dr.rect(TransparentScreen3, BuildingBeige + (bAlpha[2],),
        (120 * bComp + bShiftX[2], 176 * bComp + bShiftY[2], 35 * bComp, 150 * bComp))
dr.rect(TransparentScreen3, BuildingBeige + (bAlpha[2],),
        (200 * bComp + bShiftX[2], 176 * bComp + bShiftY[2], 35 * bComp, 150 * bComp))
dr.rect(TransparentScreen3, BuildingBeige + (bAlpha[2],),
        (280 * bComp + bShiftX[2], 176 * bComp + bShiftY[2], 35 * bComp, 150 * bComp))
dr.polygon(TransparentScreen3, RoofGray + (bAlpha[2],),
           [affinity(5, 175, bComp, bComp, bShiftX[2], bShiftY[2]),
            affinity(50, 135, bComp, bComp, bShiftX[2], bShiftY[2]),
            affinity(320, 135, bComp, bComp, bShiftX[2], bShiftY[2]),
            affinity(385, 175, bComp, bComp, bShiftX[2], bShiftY[2])], 0)

# Drawing chimneys
dr.rect(TransparentScreen3, ChimneyGray + (bAlpha[2],),
        (85 * bComp + bShiftX[2], 105 * bComp + bShiftY[2], 10 * bComp, 50 * bComp))
dr.rect(TransparentScreen3, ChimneyGray + (bAlpha[2],),
        (225 * bComp + bShiftX[2], 85 * bComp + bShiftY[2], 8 * bComp, 50 * bComp))
dr.rect(TransparentScreen3, ChimneyGray + (bAlpha[2],),
        (100 * bComp + bShiftX[2], 85 * bComp + bShiftY[2], 18 * bComp, 75 * bComp))
dr.rect(TransparentScreen3, ChimneyGray + (bAlpha[2],),
        (295 * bComp + bShiftX[2], 100 * bComp + bShiftY[2], 11 * bComp, 60 * bComp))

# Drawing balcony
dr.rect(TransparentScreen3, BalconyGray + (bAlpha[2],),
        (5 * bComp + bShiftX[2], 340 * bComp + bShiftY[2], 380 * bComp, 40 * bComp))
for j in range(10, 380, 60):
    dr.rect(TransparentScreen3, BalconyGray + (bAlpha[2],),
            (j * bComp + bShiftX[2], 300 * bComp + bShiftY[2], 10 * bComp, 40 * bComp))
dr.rect(TransparentScreen3, BalconyGray + (bAlpha[2],),
        (20 * bComp + bShiftX[2], 280 * bComp + bShiftY[2], 350 * bComp, 20 * bComp))

# Drawing windows
dr.rect(TransparentScreen3, WindowBrown + (bAlpha[2],),
        (80 * bComp + bShiftX[2], 460 * bComp + bShiftY[2], 60 * bComp, 70 * bComp))
dr.rect(TransparentScreen3, WindowBrown + (bAlpha[2],),
        (165 * bComp + bShiftX[2], 460 * bComp + bShiftY[2], 60 * bComp, 70 * bComp))
dr.rect(TransparentScreen3, WindowYellow + (bAlpha[2],),
        (250 * bComp + bShiftX[2], 460 * bComp + bShiftY[2], 60 * bComp, 70 * bComp))

# Drawing clouds
dr.ellipse(Screen, Cloud2Gray, (25, 65, 450, 60), 0)
dr.ellipse(Screen, Cloud1Gray, (260, 35, 350, 60), 0)
dr.ellipse(Screen, Cloud1Gray, (370, 115, 450, 45), 0)
dr.ellipse(Screen, Cloud1Gray, (100, 310, 550, 40), 0)

# Drawing ghosts
gComp = (1, 0.5, 0.5, 0.5, 0.5, 0.5)
gInv = (1, 1, -1, 1, 1, -1)
gShiftX = (0, 280, 380, 180, 290, 400)
gShiftY = (0, 160, 300, 310, 190, 335)

# Drawing ghost 1
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
dr.circle(Screen, GhostGray, (509, 674), 36, 0)
dr.circle(Screen, GhostGray, (484, 698), 20, 0)
dr.circle(Screen, GhostGray, (521, 645), 35, 0)

# Drawing ghosts 2-3
for i in range(3):
    # Drawing ghost body
    dr.circle(TransparentScreen1, GhostGray + (230,),
              affinity(475, 600, gComp[i] * gInv[i], gComp[i], gShiftX[i], gShiftY[i]),
              25 * gComp[i], 0)
    dr.circle(TransparentScreen1, GhostGray + (230,),
              affinity(410, 700, gComp[i] * gInv[i], gComp[i], gShiftX[i], gShiftY[i]),
              5 * gComp[i], 0)
    dr.circle(TransparentScreen1, GhostGray + (230,),
              affinity(470, 710, gComp[i] * gInv[i], gComp[i], gShiftX[i], gShiftY[i]),
              18 * gComp[i], 0)
    dr.circle(TransparentScreen1, GhostGray + (230,),
              affinity(530, 690, gComp[i] * gInv[i], gComp[i], gShiftX[i], gShiftY[i]),
              30 * gComp[i], 0)
    dr.circle(TransparentScreen1, GhostGray + (230,),
              affinity(565, 650, gComp[i] * gInv[i], gComp[i], gShiftX[i], gShiftY[i]),
              20 * gComp[i], 0)
    dr.circle(TransparentScreen1, GhostGray + (230,),
              affinity(500, 615, gComp[i] * gInv[i], gComp[i], gShiftX[i], gShiftY[i]),
              20 * gComp[i], 0)
    dr.circle(TransparentScreen1, GhostGray + (230,),
              affinity(509, 674, gComp[i] * gInv[i], gComp[i], gShiftX[i], gShiftY[i]),
              36 * gComp[i], 0)
    dr.circle(TransparentScreen1, GhostGray + (230,),
              affinity(484, 698, gComp[i] * gInv[i], gComp[i], gShiftX[i], gShiftY[i]),
              20 * gComp[i], 0)
    dr.circle(TransparentScreen1, GhostGray + (230,),
              affinity(521, 645, gComp[i] * gInv[i], gComp[i], gShiftX[i], gShiftY[i]),
              35 * gComp[i], 0)
    dr.polygon(TransparentScreen1, GhostGray + (230,),
               [affinity(450, 600, gComp[i] * gInv[i], gComp[i], gShiftX[i], gShiftY[i]),
                affinity(447, 630, gComp[i] * gInv[i], gComp[i], gShiftX[i], gShiftY[i]),
                affinity(427, 654, gComp[i] * gInv[i], gComp[i], gShiftX[i], gShiftY[i]),
                affinity(406, 698, gComp[i] * gInv[i], gComp[i], gShiftX[i], gShiftY[i]),
                affinity(414, 702, gComp[i] * gInv[i], gComp[i], gShiftX[i], gShiftY[i]),
                affinity(436, 694, gComp[i] * gInv[i], gComp[i], gShiftX[i], gShiftY[i]),
                affinity(455, 705, gComp[i] * gInv[i], gComp[i], gShiftX[i], gShiftY[i]),
                affinity(455, 700, gComp[i] * gInv[i], gComp[i], gShiftX[i], gShiftY[i]),
                affinity(485, 716, gComp[i] * gInv[i], gComp[i], gShiftX[i], gShiftY[i]),
                affinity(520, 700, gComp[i] * gInv[i], gComp[i], gShiftX[i], gShiftY[i]),
                affinity(550, 680, gComp[i] * gInv[i], gComp[i], gShiftX[i], gShiftY[i]),
                affinity(566, 664, gComp[i] * gInv[i], gComp[i], gShiftX[i], gShiftY[i]),
                affinity(574, 641, gComp[i] * gInv[i], gComp[i], gShiftX[i], gShiftY[i]),
                affinity(512, 600, gComp[i] * gInv[i], gComp[i], gShiftX[i], gShiftY[i]),
                affinity(450, 600, gComp[i] * gInv[i], gComp[i], gShiftX[i], gShiftY[i])], 0)

    # Drawing ghost eyes
    dr.circle(TransparentScreen1, GhostBlue + (230,),
              affinity(464, 596, gComp[i] * gInv[i], gComp[i], gShiftX[i], gShiftY[i]),
              6 * gComp[i], 0)
    dr.circle(TransparentScreen1, GhostBlue + (230,),
              affinity(484, 592, gComp[i] * gInv[i], gComp[i], gShiftX[i], gShiftY[i]),
              6 * gComp[i], 0)
    dr.circle(TransparentScreen1, Black + (230,),
              affinity(462, 596, gComp[i] * gInv[i], gComp[i], gShiftX[i], gShiftY[i]),
              2 * gComp[i], 0)
    dr.circle(TransparentScreen1, Black + (230,),
              affinity(482, 592, gComp[i] * gInv[i], gComp[i], gShiftX[i], gShiftY[i]),
              2 * gComp[i], 0)
    dr.polygon(TransparentScreen1, MoonGray + (230,),
               [affinity(463, 595, gComp[i] * gInv[i], gComp[i], gShiftX[i], gShiftY[i]),
                affinity(468, 592, gComp[i] * gInv[i], gComp[i], gShiftX[i], gShiftY[i]),
                affinity(469, 594, gComp[i] * gInv[i], gComp[i], gShiftX[i], gShiftY[i]),
                affinity(466, 595, gComp[i] * gInv[i], gComp[i], gShiftX[i], gShiftY[i]),
                affinity(463, 595, gComp[i] * gInv[i], gComp[i], gShiftX[i], gShiftY[i])],
               0)
    dr.polygon(TransparentScreen1, MoonGray + (230,),
               [affinity(483, 591, gComp[i] * gInv[i], gComp[i], gShiftX[i], gShiftY[i]),
                affinity(488, 588, gComp[i] * gInv[i], gComp[i], gShiftX[i], gShiftY[i]),
                affinity(488, 590, gComp[i] * gInv[i], gComp[i], gShiftX[i], gShiftY[i]),
                affinity(488, 591, gComp[i] * gInv[i], gComp[i], gShiftX[i], gShiftY[i]),
                affinity(483, 591, gComp[i] * gInv[i], gComp[i], gShiftX[i], gShiftY[i])],
               0)

# Drawing ghosts 4-6
for i in range(3, 6):
    # Drawing ghost body back
    dr.circle(TransparentScreen2, Black + (200,),
              affinity(475, 600, gComp[i] * gInv[i], gComp[i], gShiftX[i], gShiftY[i]),
              25 * gComp[i] + 1, 0)
    dr.circle(TransparentScreen2, Black + (200,),
              affinity(410, 700, gComp[i] * gInv[i], gComp[i], gShiftX[i], gShiftY[i]),
              5 * gComp[i] + 1, 0)
    dr.circle(TransparentScreen2, Black + (200,),
              affinity(470, 710, gComp[i] * gInv[i], gComp[i], gShiftX[i], gShiftY[i]),
              18 * gComp[i] + 1, 0)
    dr.circle(TransparentScreen2, Black + (200,),
              affinity(530, 690, gComp[i] * gInv[i], gComp[i], gShiftX[i], gShiftY[i]),
              30 * gComp[i] + 1, 0)
    dr.circle(TransparentScreen2, Black + (200,),
              affinity(565, 650, gComp[i] * gInv[i], gComp[i], gShiftX[i], gShiftY[i]),
              20 * gComp[i] + 1, 0)
    dr.circle(TransparentScreen2, Black + (200,),
              affinity(500, 615, gComp[i] * gInv[i], gComp[i], gShiftX[i], gShiftY[i]),
              20 * gComp[i] + 1, 0)
    dr.circle(TransparentScreen2, Black + (200,),
              affinity(509, 674, gComp[i] * gInv[i], gComp[i], gShiftX[i], gShiftY[i]),
              36 * gComp[i] + 1, 0)
    dr.circle(TransparentScreen2, Black + (200,),
              affinity(484, 698, gComp[i] * gInv[i], gComp[i], gShiftX[i], gShiftY[i]),
              20 * gComp[i] + 1, 0)
    dr.circle(TransparentScreen2, Black + (200,),
              affinity(521, 645, gComp[i] * gInv[i], gComp[i], gShiftX[i], gShiftY[i]),
              35 * gComp[i] + 1, 0)
    dr.polygon(TransparentScreen2, Black + (200,),
               [affinity(448, 600, gComp[i] * gInv[i], gComp[i], gShiftX[i], gShiftY[i]),
                affinity(445, 629, gComp[i] * gInv[i], gComp[i], gShiftX[i], gShiftY[i]),
                affinity(425, 652, gComp[i] * gInv[i], gComp[i], gShiftX[i], gShiftY[i]),
                affinity(404, 698, gComp[i] * gInv[i], gComp[i], gShiftX[i], gShiftY[i]),
                affinity(416, 702, gComp[i] * gInv[i], gComp[i], gShiftX[i], gShiftY[i]),
                affinity(436, 694, gComp[i] * gInv[i], gComp[i], gShiftX[i], gShiftY[i]),
                affinity(455, 705, gComp[i] * gInv[i], gComp[i], gShiftX[i], gShiftY[i]),
                affinity(455, 700, gComp[i] * gInv[i], gComp[i], gShiftX[i], gShiftY[i]),
                affinity(485, 718, gComp[i] * gInv[i], gComp[i], gShiftX[i], gShiftY[i]),
                affinity(520, 702, gComp[i] * gInv[i], gComp[i], gShiftX[i], gShiftY[i]),
                affinity(550, 682, gComp[i] * gInv[i], gComp[i], gShiftX[i], gShiftY[i]),
                affinity(566, 664, gComp[i] * gInv[i], gComp[i], gShiftX[i], gShiftY[i]),
                affinity(576, 641, gComp[i] * gInv[i], gComp[i], gShiftX[i], gShiftY[i]),
                affinity(514, 600, gComp[i] * gInv[i], gComp[i], gShiftX[i], gShiftY[i]),
                affinity(450, 600, gComp[i] * gInv[i], gComp[i], gShiftX[i], gShiftY[i])], 0)

    # Drawing ghost body
    dr.circle(TransparentScreen2, GhostGray + (200,),
              affinity(475, 600, gComp[i] * gInv[i], gComp[i], gShiftX[i], gShiftY[i]),
              25 * gComp[i], 0)
    dr.circle(TransparentScreen2, GhostGray + (200,),
              affinity(410, 700, gComp[i] * gInv[i], gComp[i], gShiftX[i], gShiftY[i]),
              5 * gComp[i], 0)
    dr.circle(TransparentScreen2, GhostGray + (200,),
              affinity(470, 710, gComp[i] * gInv[i], gComp[i], gShiftX[i], gShiftY[i]),
              18 * gComp[i], 0)
    dr.circle(TransparentScreen2, GhostGray + (200,),
              affinity(530, 690, gComp[i] * gInv[i], gComp[i], gShiftX[i], gShiftY[i]),
              30 * gComp[i], 0)
    dr.circle(TransparentScreen2, GhostGray + (200,),
              affinity(565, 650, gComp[i] * gInv[i], gComp[i], gShiftX[i], gShiftY[i]),
              20 * gComp[i], 0)
    dr.circle(TransparentScreen2, GhostGray + (200,),
              affinity(500, 615, gComp[i] * gInv[i], gComp[i], gShiftX[i], gShiftY[i]),
              20 * gComp[i], 0)
    dr.circle(TransparentScreen2, GhostGray + (200,),
              affinity(509, 674, gComp[i] * gInv[i], gComp[i], gShiftX[i], gShiftY[i]),
              36 * gComp[i], 0)
    dr.circle(TransparentScreen2, GhostGray + (200,),
              affinity(484, 698, gComp[i] * gInv[i], gComp[i], gShiftX[i], gShiftY[i]),
              20 * gComp[i], 0)
    dr.circle(TransparentScreen2, GhostGray + (200,),
              affinity(521, 645, gComp[i] * gInv[i], gComp[i], gShiftX[i], gShiftY[i]),
              35 * gComp[i], 0)
    dr.polygon(TransparentScreen2, GhostGray + (200,),
               [affinity(450, 600, gComp[i] * gInv[i], gComp[i], gShiftX[i], gShiftY[i]),
                affinity(447, 630, gComp[i] * gInv[i], gComp[i], gShiftX[i], gShiftY[i]),
                affinity(427, 654, gComp[i] * gInv[i], gComp[i], gShiftX[i], gShiftY[i]),
                affinity(406, 698, gComp[i] * gInv[i], gComp[i], gShiftX[i], gShiftY[i]),
                affinity(414, 702, gComp[i] * gInv[i], gComp[i], gShiftX[i], gShiftY[i]),
                affinity(436, 694, gComp[i] * gInv[i], gComp[i], gShiftX[i], gShiftY[i]),
                affinity(455, 705, gComp[i] * gInv[i], gComp[i], gShiftX[i], gShiftY[i]),
                affinity(455, 700, gComp[i] * gInv[i], gComp[i], gShiftX[i], gShiftY[i]),
                affinity(485, 716, gComp[i] * gInv[i], gComp[i], gShiftX[i], gShiftY[i]),
                affinity(520, 700, gComp[i] * gInv[i], gComp[i], gShiftX[i], gShiftY[i]),
                affinity(550, 680, gComp[i] * gInv[i], gComp[i], gShiftX[i], gShiftY[i]),
                affinity(566, 664, gComp[i] * gInv[i], gComp[i], gShiftX[i], gShiftY[i]),
                affinity(574, 641, gComp[i] * gInv[i], gComp[i], gShiftX[i], gShiftY[i]),
                affinity(512, 600, gComp[i] * gInv[i], gComp[i], gShiftX[i], gShiftY[i]),
                affinity(450, 600, gComp[i] * gInv[i], gComp[i], gShiftX[i], gShiftY[i])], 0)

    # Drawing ghost eyes
    dr.circle(TransparentScreen2, GhostBlue + (200,),
              affinity(464, 596, gComp[i] * gInv[i], gComp[i], gShiftX[i], gShiftY[i]),
              6 * gComp[i], 0)
    dr.circle(TransparentScreen2, GhostBlue + (200,),
              affinity(484, 592, gComp[i] * gInv[i], gComp[i], gShiftX[i], gShiftY[i]),
              6 * gComp[i], 0)
    dr.circle(TransparentScreen2, Black + (200,),
              affinity(462, 596, gComp[i] * gInv[i], gComp[i], gShiftX[i], gShiftY[i]),
              2 * gComp[i], 0)
    dr.circle(TransparentScreen2, Black + (200,),
              affinity(482, 592, gComp[i] * gInv[i], gComp[i], gShiftX[i], gShiftY[i]),
              2 * gComp[i], 0)
    dr.polygon(TransparentScreen2, MoonGray + (200,),
               [affinity(463, 595, gComp[i] * gInv[i], gComp[i], gShiftX[i], gShiftY[i]),
                affinity(468, 592, gComp[i] * gInv[i], gComp[i], gShiftX[i], gShiftY[i]),
                affinity(469, 594, gComp[i] * gInv[i], gComp[i], gShiftX[i], gShiftY[i]),
                affinity(466, 595, gComp[i] * gInv[i], gComp[i], gShiftX[i], gShiftY[i]),
                affinity(463, 595, gComp[i] * gInv[i], gComp[i], gShiftX[i], gShiftY[i])],
               0)
    dr.polygon(TransparentScreen2, MoonGray + (200,),
               [affinity(483, 591, gComp[i] * gInv[i], gComp[i], gShiftX[i], gShiftY[i]),
                affinity(488, 588, gComp[i] * gInv[i], gComp[i], gShiftX[i], gShiftY[i]),
                affinity(488, 590, gComp[i] * gInv[i], gComp[i], gShiftX[i], gShiftY[i]),
                affinity(488, 591, gComp[i] * gInv[i], gComp[i], gShiftX[i], gShiftY[i]),
                affinity(483, 591, gComp[i] * gInv[i], gComp[i], gShiftX[i], gShiftY[i])],
               0)

Screen.blit(TransparentScreen1, (0, 0))
Screen.blit(TransparentScreen2, (0, 0))
Screen.blit(TransparentScreen3, (0, 0))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()