import numpy as np

N = int(input())

F = np.zeros(2)

for i in range(N):
    x, y, f_abs = (float(x) for x in input().split())
    F += np.array([x, y]) / (x ** 2 + y ** 2) ** 0.5 * f_abs

for coord in F:
    print(f"{coord:.4f}", end=' ')
