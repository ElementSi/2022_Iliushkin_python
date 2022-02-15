import turtle as trt
import math as math

trt.shape('turtle')
trt.speed(0)

angle = 0
step = 2
dAngleDeg = 1
dAngleRad = dAngleDeg / 360 * 2 * math.pi

for i in range(3600):
    angle = angle + dAngleRad
    trt.left(dAngleDeg)
    trt.forward(step * dAngleRad * (1 + angle ** 2) ** 0.5)
