import turtle as trt
import math as math

trt.shape('turtle')
trt.speed(0)


def arc(rad, angle, split):
    for j in range(int(angle / 360 * split)):
        trt.forward(rad * 2 * math.pi / split)
        trt.right(360 / split)


Split = 180
NumOfLinks = 4
Rad1 = 40
Rad2 = 8

trt.left(90)
for i in range(NumOfLinks):
    arc(Rad1, 180, Split)
    arc(Rad2, 180, Split)
