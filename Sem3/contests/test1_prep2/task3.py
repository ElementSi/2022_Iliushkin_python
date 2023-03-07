data = input().split()
minx = float(data[0])
maxx = float(data[1])

data = input().split()
miny = float(data[0])
maxy = float(data[1])

data = input().split()
minz = float(data[0])
maxz = float(data[1])

n = int(input())
res = []
for _ in range(n):
    dot = input().split()
    x = float(dot[0])
    y = float(dot[1])
    z = float(dot[2])
    if minx <= x <= maxx and miny <= y <= maxy and minz <= z <= maxz:
        res.append((x, y, z))

print(len(res))
