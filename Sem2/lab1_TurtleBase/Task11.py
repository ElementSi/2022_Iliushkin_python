import turtle as trt
import math as math

trt.shape('turtle')
trt.speed(0)


def circle(rad, split):
    for j in range(split):
        trt.forward(rad * 2 * math.pi / split)
        trt.right(360 / split)


Split = 180
NumOfLayers = 6
Step = 10

trt.right(90)
for i in range(6, NumOfLayers * 2 + 6):
    if i % 2 == 0:
        circle(i * Step / 2, Split)
    else:
        circle((i - 1) * Step / 2, Split)
    trt.right(180)
