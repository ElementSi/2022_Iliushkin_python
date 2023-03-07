import numpy as np

N, M = (int(x) for x in input().split())
K = int(input())

field = np.zeros((N, M), dtype=int)

for i in range(K):
    lamp_x, lamp_y = (int(x) for x in input().split())
    field[:, lamp_y] += 1
    field[lamp_x, :] += 1
    field[lamp_x, lamp_y] -= 1

print(np.count_nonzero(field > 1))
