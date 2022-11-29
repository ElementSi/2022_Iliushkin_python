width, height = [int(x) for x in input().split(" ")]

field = []
for i in range(height):
    field.append(input())

x_hedgehog, y_hedgehog, vis_range = [int(x) for x in input().split(" ")]

for y in range(max(0, y_hedgehog - vis_range), min(height, y_hedgehog + vis_range + 1)):
    print(field[y][max(0, x_hedgehog - vis_range):min(width, x_hedgehog + vis_range + 1)])
