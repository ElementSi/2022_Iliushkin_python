import turtle as trt

n = int(input())

trt.shape('turtle')

for i in range(n):
    trt.right(360 / n)
    trt.forward(100)
    trt.stamp()
    trt.right(180)
    trt.forward(100)
    trt.right(180)
