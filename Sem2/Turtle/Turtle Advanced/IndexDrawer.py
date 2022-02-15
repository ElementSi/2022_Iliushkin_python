import turtle as trt

trt.shape('turtle')
trt.speed(1)


def draw(direct, shift):
    x = trt.xcor()
    y = trt.ycor()
    if direct == 'up':
        trt.goto(x, y + shift)
    elif direct == 'down':
        trt.goto(x, y - shift)
    elif direct == 'left':
        trt.goto(x - shift, y)
    elif direct == 'right':
        trt.goto(x + shift, y)
    elif direct == 'rightup':
        trt.goto(x + shift, y + shift)
    elif direct == 'rightdown':
        trt.goto(x + shift, y - shift)
    elif direct == 'leftup':
        trt.goto(x - shift, y + shift)
    elif direct == 'leftdown':
        trt.goto(x - shift, y - shift)


def move(direct, shift):
    trt.penup()
    draw(direct, shift)
    trt.pendown()


Fontsize = 40

Fig0 = ((1, 1, 1, 1, 0), ('down', 'right', 'up', 'left', 'right'), (2, 1, 2, 1, 2))
Fig1 = ((0, 1, 1, 0, 0), ('down', 'rightup', 'down', 'rightup', 'up'), (1, 1, 2, 1, 1))
Fig2 = ((1, 1, 1, 1, 0, 0), ('right', 'down', 'leftdown', 'right', 'rightup', 'up'), (1, 1, 1, 1, 1, 1))
Fig3 = ((1, 1, 1, 1, 0), ('right', 'leftdown', 'right', 'leftdown', 'rightup'), (1, 1, 1, 1, 2))
Fig4 = ((1, 1, 1, 1, 0, 0), ('down', 'right', 'up', 'down', 'rightup', 'up'), (1, 1, 1, 2, 1, 1))
Fig5 = ((0, 1, 1, 1, 1, 1, 0), ('right', 'left', 'down', 'right', 'down', 'left', 'rightup'), (1, 1, 1, 1, 1, 1, 2))
Fig6 = ((0, 1, 1, 1, 1, 1, 0, 0), ('right', 'leftdown', 'down', 'right', 'up', 'left', 'right', 'rightup'),
        (1, 1, 1, 1, 1, 1, 1, 1))
Fig7 = ((1, 1, 1, 0), ('right', 'leftdown', 'down', 'rightup'), (1, 1, 1, 2))
Fig8 = ((1, 1, 1, 1, 1, 1, 0), ('right', 'down', 'left', 'up', 'down', 'right', 'rightup'), (1, 2, 1, 2, 1, 1, 1))
Fig9 = ((0, 1, 1, 1, 1, 1, 0), ('down', 'rightup', 'up', 'left', 'down', 'right', 'rightup'), (2, 1, 1, 1, 1, 1, 1))

Figs = [Fig0, Fig1, Fig2, Fig3, Fig4, Fig5, Fig6, Fig7, Fig8, Fig9]

Index = (list(input('Enter the index: ')))
if len(Index) != 6:
    exit('Incorrect index!')
for i in range(6):
    Index[i] = int(Index[i])

move('left', Fontsize * 5.5)
move('up', Fontsize)
for i in Index:
    for j in range(len(Figs[i][0])):
        if Figs[i][0][j]:
            draw(Figs[i][1][j], Fontsize * Figs[i][2][j])
        else:
            move(Figs[i][1][j], Fontsize * Figs[i][2][j])
