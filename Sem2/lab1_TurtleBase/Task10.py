import turtle as trt
import math as math

trt.shape('turtle')
trt.speed(0)


def circle(rad, split):
    for j in range(split):
        trt.right(360 / split)
        trt.forward(rad * 2 * math.pi / split)


Split = 180
NumOfPetals = 6
Rad = 50

for i in range(NumOfPetals):
    circle(Rad, Split)
    trt.right(360 / NumOfPetals)
