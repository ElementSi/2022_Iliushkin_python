import turtle as trt
import math as math

trt.shape('turtle')
trt.speed(5)


def star(edge, corners):
    trt.right(90 - 90 / corners)
    for j in range(corners):
        trt.forward(edge)
        trt.right(180 - 180 / corners)


Edge = 200
NumOfCorners = int(input('Enter number of corners:'))

star(Edge, NumOfCorners)
