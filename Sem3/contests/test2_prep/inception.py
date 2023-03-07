import numpy as np


N = int(input())
u_before = np.array([float(i) for i in input().split()]).T
R_py = []
for i in range(N):
    row = [float(i) for i in input().split()]
    R_py.append(row)
    
R = np.array(R_py)

k = int(input())
for i in range(k):
    u_before = R @ u_before

for i in u_before:
    print(f"{i:.4f}", end=' ')
