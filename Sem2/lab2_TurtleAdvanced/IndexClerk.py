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

Figs = [[['0' for i in range(8)] for j in range(3)] for k in range(10)]

with open('IndexFont.txt') as file:
    SubFigs = file.readlines()
    for i in range(len(SubFigs)):
        for j in range(3):
            Figs[i][j] = SubFigs[i].split(';')[j].split(',')

Index = (list(input('Enter the index: ')))
if len(Index) != 6:
    exit('Incorrect index!')
for i in range(6):
    Index[i] = int(Index[i])

move('left', Fontsize * 5.5)
move('up', Fontsize)
for i in Index:
    for j in range(len(Figs[i][0])):
        if int(Figs[i][0][j]):
            draw(Figs[i][1][j], Fontsize * int(Figs[i][2][j]))
        else:
            move(Figs[i][1][j], Fontsize * int(Figs[i][2][j]))
