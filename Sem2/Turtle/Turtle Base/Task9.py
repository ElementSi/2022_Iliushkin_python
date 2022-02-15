import turtle as trt
import math as math


def n_angle(n):
    trt.penup()
    side = (n-2)*10 * (2*math.sin(math.pi/n))
    trt.forward(10)
    trt.right(90 - 360/(2*n))
    trt.pendown()
    for i in range(n):
        trt.right(360 / n)
        trt.forward(side)
    trt.left(90 - 360/(2*n))


trt.shape('turtle')
trt.speed(0)

for j in range(3, 30):
    n_angle(j)
