class Ball:
    def __init__(self, x, y, m):
        if m <= 0:
            raise Exception('RuntimeError')
        self.m = m
        self.x = x
        self.y = y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy


b = Ball(0.0, 0.0, 1.0)
print(b.x, b.y, b.m)
b.move(1.0, -1.0)
print(b.x, b.y, b.m)
