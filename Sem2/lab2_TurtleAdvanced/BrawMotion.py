import turtle as trt
import random as rand

trt.shape('turtle')
trt.speed(0)

while True:
    trt.forward(rand.randint(0, 20))
    trt.right(rand.randint(0, 360))
