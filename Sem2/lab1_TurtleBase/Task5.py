import turtle as trt

trt.shape('turtle')
trt.speed(0)

for i in range(10, 1001, 10):
    trt.penup()
    trt.right(90)
    trt.forward(5)
    trt.right(90)
    trt.forward(5)
    trt.right(180)
    trt.pendown()

    trt.forward(i)
    trt.left(90)
    trt.forward(i)
    trt.left(90)
    trt.forward(i)
    trt.left(90)
    trt.forward(i)
    trt.left(90)
