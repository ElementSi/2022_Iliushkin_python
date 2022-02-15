import turtle as trt
import math as math

trt.shape('turtle')
trt.speed(0)


def arc(rad, angle, split):
    for j in range(int(angle / 360 * split)):
        trt.forward(rad * 2 * math.pi / split)
        trt.right(360 / split)


def arcl(rad, angle, split):
    for j in range(int(angle / 360 * split)):
        trt.forward(rad * 2 * math.pi / split)
        trt.left(360 / split)


def circle(rad, split):
    for j in range(split):
        trt.forward(rad * 2 * math.pi / split)
        trt.right(360 / split)


Split = 60
RadFace = 100
RadEye = 10
LengthNose = 20
RadSmile = 90
AngleSmile = 100

# Drawing face
trt.penup()
trt.goto(0, RadFace)
trt.pendown()
trt.begin_fill()
circle(RadFace, Split)
trt.color('#f4d500')
trt.end_fill()
trt.color('#000000')

# Drawing 1st eye
trt.penup()
trt.goto(- RadFace / 3, RadFace / 4 + RadEye)
trt.pendown()
trt.begin_fill()
circle(RadEye, Split)
trt.end_fill()

# Drawing 2nd eye
trt.penup()
trt.goto(RadFace / 3, RadFace / 4 + RadEye)
trt.pendown()
trt.begin_fill()
circle(RadEye, Split)
trt.end_fill()

# Drawing nose
trt.penup()
trt.goto(0, 0)
trt.pendown()
trt.width(10)
trt.right(90)
trt.forward(LengthNose)

# Drawing smile
trt.width(6)
trt.penup()
trt.goto(0, - RadFace / 2)
trt.pendown()
trt.setheading(0)
arcl(RadSmile, AngleSmile / 2, Split)
trt.penup()
trt.goto(0, - RadFace / 2)
trt.pendown()
trt.setheading(180)
arc(RadSmile, AngleSmile / 2, Split)
