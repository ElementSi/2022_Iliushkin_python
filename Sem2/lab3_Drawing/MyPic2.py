import pygame
import pygame.draw as dr

pygame.init()

# Setting up and creating multiple screenshots to ensure transparency
FPS = 30
Screen = pygame.display.set_mode((600, 800))
TransparentScreen0 = pygame.Surface((600, 800), pygame.SRCALPHA)
TransparentScreen1 = pygame.Surface((600, 800), pygame.SRCALPHA)
TransparentScreen2 = pygame.Surface((600, 800), pygame.SRCALPHA)

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


def affinity(x, y, kx, ky, dx, dy):
    """
    This function performs an affine transformation of the coordinate data.
    Type of affine transformation:
        x' = kx * x + dx
        y' = ky * y + dy
    :param x: the initial x coordinate
    :param y: the initial y coordinate
    :param kx: coefficient at x
    :param ky: coefficient at y
    :param dx: free member at x
    :param dy: free member at y
    :return: list of received coordinates - [x' , y']
    """
    x = x * kx + dx
    y = y * ky + dy
    return [x, y]


def draw_background(ground_color, sky_color, moon_color, cloud_color):
    """
    This function draws the background: ground, sky, full moon and one cloud.
    :param ground_color: the color of the ground
    :param sky_color: the color of the sky
    :param moon_color: the color of the moon
    :param cloud_color: the color of the cloud
    :return: nothing
    """
    Screen.fill(ground_color)
    dr.rect(Screen, sky_color, (0, 0, 600, 330))
    dr.circle(Screen, moon_color, (540, 70), 50, 0)
    dr.ellipse(Screen, cloud_color, (300, 200, 500, 50), 0)


def draw_base(screen, shift_x, shift_y, size, transparency):
    """
    This function draws a base for drawing a building: a wall and... windows?
    :param screen: the screen on which all the elements of the base are drawn
    :param shift_x: shift by x from the default value
    :param shift_y: shift by y from the default value
    :param size: the size of the base
    :param transparency: transparency of the base. Maximum - 255
    :return: nothing
    """
    dr.rect(screen, BuildingBrown + (transparency,),
            (40 * size + shift_x, 175 * size + shift_y, 310 * size, 400 * size))
    dr.rect(screen, BuildingBeige + (transparency,),
            (60 * size + shift_x, 176 * size + shift_y, 35 * size, 150 * size))
    dr.rect(screen, BuildingBeige + (transparency,),
            (120 * size + shift_x, 176 * size + shift_y, 35 * size, 150 * size))
    dr.rect(screen, BuildingBeige + (transparency,),
            (200 * size + shift_x, 176 * size + shift_y, 35 * size, 150 * size))
    dr.rect(screen, BuildingBeige + (transparency,),
            (280 * size + shift_x, 176 * size + shift_y, 35 * size, 150 * size))


def draw_roof_with_chimneys(screen, shift_x, shift_y, size, transparency):
    """
    This function draws a roof with 4 chimneys.
    :param screen: the screen on which all the elements of the roof with chimneys are drawn
    :param shift_x: shift by x from the default value
    :param shift_y: shift by y from the default value
    :param size: the size of the roof with chimneys
    :param transparency: transparency of the roof with chimneys. Maximum - 255
    :return: nothing
    """
    dr.polygon(screen, RoofGray + (transparency,),
               [affinity(5, 175, size, size, shift_x, shift_y),
                affinity(50, 135, size, size, shift_x, shift_y),
                affinity(320, 135, size, size, shift_x, shift_y),
                affinity(385, 175, size, size, shift_x, shift_y)], 0)

    dr.rect(screen, ChimneyGray + (transparency,),
            (85 * size + shift_x, 105 * size + shift_y, 10 * size, 50 * size))
    dr.rect(screen, ChimneyGray + (transparency,),
            (225 * size + shift_x, 85 * size + shift_y, 8 * size, 50 * size))
    dr.rect(screen, ChimneyGray + (transparency,),
            (100 * size + shift_x, 85 * size + shift_y, 18 * size, 75 * size))
    dr.rect(screen, ChimneyGray + (transparency,),
            (295 * size + shift_x, 100 * size + shift_y, 11 * size, 60 * size))


def draw_balcony(screen, shift_x, shift_y, size, transparency):
    """
    This function draws a balcony with a crossbar.
    :param screen: the screen on which all the elements of the balcony are drawn
    :param shift_x: shift by x from the default value
    :param shift_y: shift by y from the default value
    :param size: the size of the balcony
    :param transparency: transparency of the balcony. Maximum - 255
    :return: nothing
    """
    dr.rect(screen, BalconyGray + (transparency,),
            (5 * size + shift_x, 340 * size + shift_y, 380 * size, 40 * size))
    for j in range(10, 380, 60):
        dr.rect(screen, BalconyGray + (transparency,),
                (j * size + shift_x, 300 * size + shift_y, 10 * size, 40 * size))
    dr.rect(screen, BalconyGray + (transparency,),
            (20 * size + shift_x, 280 * size + shift_y, 350 * size, 20 * size))


def draw_windows(screen, shift_x, shift_y, size, transparency):
    """
    This function draws three windows.
    :param screen: the screen on which all the elements of the windows are drawn
    :param shift_x: shift by x from the default value
    :param shift_y: shift by y from the default value
    :param size: the size of the windows
    :param transparency: transparency of the windows. Maximum - 255
    :return: nothing
    """
    dr.rect(screen, WindowBrown + (transparency,),
            (80 * size + shift_x, 460 * size + shift_y, 60 * size, 70 * size))
    dr.rect(screen, WindowBrown + (transparency,),
            (165 * size + shift_x, 460 * size + shift_y, 60 * size, 70 * size))
    dr.rect(screen, WindowYellow + (transparency,),
            (250 * size + shift_x, 460 * size + shift_y, 60 * size, 70 * size))


def draw_building(screen, shift_x, shift_y, size, transparency):
    """
    This function draws a building with a roof, chimneys, balcony and windows.
    :param screen: the screen on which all the elements of the building are drawn
    :param shift_x: shift by x from the default value
    :param shift_y: shift by y from the default value
    :param size: the size of the building
    :param transparency: transparency of the building. Maximum - 255
    :return: nothing
    """
    size = size * 0.45
    draw_base(screen, shift_x, shift_y, size, transparency)
    draw_roof_with_chimneys(screen, shift_x, shift_y, size, transparency)
    draw_balcony(screen, shift_x, shift_y, size, transparency)
    draw_windows(screen, shift_x, shift_y, size, transparency)


def draw_cloud(screen, color, transparency, x, y, a, b):
    """
    This function draws a transparent cloud.
    :param screen: the screen on which the cloud will be drawn
    :param color: cloud color
    :param transparency: cloud transparency, maximum 255
    :param x: the x coordinate of the upper-left vertex of the rectangle in which the cloud will be drawn
    :param y: the y coordinate of the upper-left vertex of the rectangle in which the cloud will be drawn
    :param a: the width of the rectangle in which the cloud will be drawn
    :param b: the height of the rectangle in which the cloud will be drawn
    :return: nothing
    """
    dr.ellipse(screen, color + (transparency,), (x, y, a, b))


def draw_ghost_body(screen, shift_x, shift_y, size, transparency, mirror):
    """
    This function draws a transparent ghost body, similar to a flying sheet.
    :param screen: the screen on which the ghost body will be drawn
    :param shift_x: shift by x from the default value
    :param shift_y: shift by y from the default value
    :param size: the size of the ghost body
    :param transparency: transparency of the ghost body. Maximum - 255
    :param mirror: If 1, the ghost's body is directed to the left, if -1 to the right.
    :return: nothing
    """
    dr.circle(screen, GhostGray + (transparency,),
              affinity(475, 600, size * mirror, size, shift_x, shift_y),
              25 * size, 0)
    dr.circle(screen, GhostGray + (transparency,),
              affinity(410, 700, size * mirror, size, shift_x, shift_y),
              5 * size, 0)
    dr.circle(screen, GhostGray + (transparency,),
              affinity(470, 710, size * mirror, size, shift_x, shift_y),
              18 * size, 0)
    dr.circle(screen, GhostGray + (transparency,),
              affinity(530, 690, size * mirror, size, shift_x, shift_y),
              30 * size, 0)
    dr.circle(screen, GhostGray + (transparency,),
              affinity(565, 650, size * mirror, size, shift_x, shift_y),
              20 * size, 0)
    dr.circle(screen, GhostGray + (transparency,),
              affinity(500, 615, size * mirror, size, shift_x, shift_y),
              20 * size, 0)
    dr.circle(screen, GhostGray + (transparency,),
              affinity(509, 674, size * mirror, size, shift_x, shift_y),
              36 * size, 0)
    dr.circle(screen, GhostGray + (transparency,),
              affinity(484, 698, size * mirror, size, shift_x, shift_y),
              20 * size, 0)
    dr.circle(screen, GhostGray + (transparency,),
              affinity(521, 645, size * mirror, size, shift_x, shift_y),
              35 * size, 0)
    dr.polygon(screen, GhostGray + (transparency,),
               [affinity(450, 600, size * mirror, size, shift_x, shift_y),
                affinity(447, 630, size * mirror, size, shift_x, shift_y),
                affinity(427, 654, size * mirror, size, shift_x, shift_y),
                affinity(406, 698, size * mirror, size, shift_x, shift_y),
                affinity(414, 702, size * mirror, size, shift_x, shift_y),
                affinity(436, 694, size * mirror, size, shift_x, shift_y),
                affinity(455, 705, size * mirror, size, shift_x, shift_y),
                affinity(455, 700, size * mirror, size, shift_x, shift_y),
                affinity(485, 716, size * mirror, size, shift_x, shift_y),
                affinity(520, 700, size * mirror, size, shift_x, shift_y),
                affinity(550, 680, size * mirror, size, shift_x, shift_y),
                affinity(566, 664, size * mirror, size, shift_x, shift_y),
                affinity(574, 641, size * mirror, size, shift_x, shift_y),
                affinity(512, 600, size * mirror, size, shift_x, shift_y),
                affinity(450, 600, size * mirror, size, shift_x, shift_y)], 0)


def draw_ghost_body_outline(screen, shift_x, shift_y, size, transparency, mirror):
    """
    This function draws the outline of the ghost's body.
    :param screen: the screen on which the outline will be drawn
    :param shift_x: shift by x from the default value
    :param shift_y: shift by y from the default value
    :param size: the size of the outline
    :param transparency: transparency of the outline. Maximum - 255
    :param mirror: If 1, the outline is directed to the left, if -1 to the right.
    :return: nothing
    """
    dr.circle(screen, Black + (transparency,),
              affinity(475, 600, size * mirror, size, shift_x, shift_y),
              25 * size + 1, 1)
    dr.circle(screen, Black + (transparency,),
              affinity(410, 700, size * mirror, size, shift_x, shift_y),
              5 * size + 1, 1)
    dr.circle(screen, Black + (transparency,),
              affinity(470, 710, size * mirror, size, shift_x, shift_y),
              18 * size + 1, 1)
    dr.circle(screen, Black + (transparency,),
              affinity(530, 690, size * mirror, size, shift_x, shift_y),
              30 * size + 1, 1)
    dr.circle(screen, Black + (transparency,),
              affinity(565, 650, size * mirror, size, shift_x, shift_y),
              20 * size + 1, 1)
    dr.circle(screen, Black + (transparency,),
              affinity(500, 615, size * mirror, size, shift_x, shift_y),
              20 * size + 1, 1)
    dr.circle(screen, Black + (transparency,),
              affinity(509, 674, size * mirror, size, shift_x, shift_y),
              36 * size + 1, 1)
    dr.circle(screen, Black + (transparency,),
              affinity(484, 698, size * mirror, size, shift_x, shift_y),
              20 * size + 1, 1)
    dr.circle(screen, Black + (transparency,),
              affinity(521, 645, size * mirror, size, shift_x, shift_y),
              35 * size + 1, 1)
    dr.polygon(screen, Black + (transparency,),
               [affinity(448, 600, size * mirror, size, shift_x, shift_y),
                affinity(445, 629, size * mirror, size, shift_x, shift_y),
                affinity(425, 652, size * mirror, size, shift_x, shift_y),
                affinity(404, 698, size * mirror, size, shift_x, shift_y),
                affinity(416, 702, size * mirror, size, shift_x, shift_y),
                affinity(436, 694, size * mirror, size, shift_x, shift_y),
                affinity(455, 705, size * mirror, size, shift_x, shift_y),
                affinity(455, 700, size * mirror, size, shift_x, shift_y),
                affinity(485, 718, size * mirror, size, shift_x, shift_y),
                affinity(520, 702, size * mirror, size, shift_x, shift_y),
                affinity(550, 682, size * mirror, size, shift_x, shift_y),
                affinity(566, 664, size * mirror, size, shift_x, shift_y),
                affinity(576, 641, size * mirror, size, shift_x, shift_y),
                affinity(514, 600, size * mirror, size, shift_x, shift_y),
                affinity(450, 600, size * mirror, size, shift_x, shift_y)], 1)


def draw_ghost_eyes(screen, shift_x, shift_y, size, transparency, mirror):
    """
    This function draws the ghost's eyes with a glint.
    :param screen: the screen on which the ghost's eyes will be drawn
    :param shift_x: shift by x from the default value
    :param shift_y: shift by y from the default value
    :param size: the size of the ghost's eyes
    :param transparency: transparency of the ghost's eyes. Maximum - 255
    :param mirror: If 1, the ghost's eyes is directed to the left, if -1 to the right.
    :return: nothing
    """
    dr.circle(screen, GhostBlue + (transparency,),
              affinity(464, 596, size * mirror, size, shift_x, shift_y),
              6 * size, 0)
    dr.circle(screen, GhostBlue + (transparency,),
              affinity(484, 592, size * mirror, size, shift_x, shift_y),
              6 * size, 0)
    dr.circle(screen, Black + (transparency,),
              affinity(462, 596, size * mirror, size, shift_x, shift_y),
              2 * size, 0)
    dr.circle(screen, Black + (transparency,),
              affinity(482, 592, size * mirror, size, shift_x, shift_y),
              2 * size, 0)
    dr.polygon(screen, MoonGray + (transparency,),
               [affinity(463, 595, size * mirror, size, shift_x, shift_y),
                affinity(468, 592, size * mirror, size, shift_x, shift_y),
                affinity(469, 594, size * mirror, size, shift_x, shift_y),
                affinity(466, 595, size * mirror, size, shift_x, shift_y),
                affinity(463, 595, size * mirror, size, shift_x, shift_y)],
               0)
    dr.polygon(screen, MoonGray + (transparency,),
               [affinity(483, 591, size * mirror, size, shift_x, shift_y),
                affinity(488, 588, size * mirror, size, shift_x, shift_y),
                affinity(488, 590, size * mirror, size, shift_x, shift_y),
                affinity(488, 591, size * mirror, size, shift_x, shift_y),
                affinity(483, 591, size * mirror, size, shift_x, shift_y)],
               0)


def draw_ghost(screen, shift_x, shift_y, size, transparency, mirror, outline):
    """
    This function draws a ghost.
    :param screen: the screen on which the ghost will be drawn
    :param shift_x: shift by x from the default value
    :param shift_y: shift by y from the default value
    :param size: the size of the ghost
    :param transparency: transparency of the ghost. Maximum - 255
    :param mirror: If 1, the ghost is directed to the left, if -1 to the right.
    :param outline: If True, then draws a outline to the cast.
    :return: nothing
    """
    if outline:
        draw_ghost_body_outline(screen, shift_x, shift_y, size, transparency, mirror)
    draw_ghost_body(screen, shift_x, shift_y, size, transparency, mirror)
    draw_ghost_eyes(screen, shift_x, shift_y, size, transparency, mirror)


draw_background(Black, SkyGray, MoonGray, Cloud3Gray)

# Drawing buildings
bComp = 1
bShiftX = (430, 180, 0)
bShiftY = (130, 230, 300)
bAlpha = (128, 200, 255)

for i in range(0, 3):
    if i == 2:
        bScreen = TransparentScreen2
    else:
        bScreen = TransparentScreen0
    draw_building(bScreen, bShiftX[i], bShiftY[i], bComp, bAlpha[i])

# Drawing special in building clouds
draw_cloud(TransparentScreen1, Cloud2Gray, 200, -65, 430, 350, 40)
draw_cloud(TransparentScreen1, Cloud2Gray, 200, 260, 380, 400, 45)

# Drawing clouds
draw_cloud(Screen, Cloud2Gray, 0, 25, 65, 450, 60)
draw_cloud(Screen, Cloud1Gray, 0, 260, 35, 350, 60)
draw_cloud(Screen, Cloud1Gray, 0, 370, 115, 450, 45)
draw_cloud(Screen, Cloud1Gray, 0, 100, 310, 550, 40)

# Drawing ghosts
gComp = (1, 0.5, 0.5, 0.5, 0.5, 0.5)
gInv = (1, 1, -1, 1, 1, -1)
gShiftX = (0, 280, 380, 180, 290, 400)
gShiftY = (0, 160, 300, 310, 190, 335)

# Drawing ghosts 1-3
for i in range(3):
    draw_ghost(TransparentScreen0, gShiftX[i], gShiftY[i], gComp[i], 230, gInv[i], False)

# Drawing ghosts 4-6
for i in range(3, 6):
    draw_ghost(TransparentScreen2, gShiftX[i], gShiftY[i], gComp[i], 200, gInv[i], True)

Screen.blit(TransparentScreen0, (0, 0))
Screen.blit(TransparentScreen1, (0, 0))
Screen.blit(TransparentScreen2, (0, 0))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
