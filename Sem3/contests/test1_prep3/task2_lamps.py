N, M = [int(x) for x in input().split(' ')]
A = []
for i in range(M):
    A.append([0] * N)

K = int(input())
for i in range(K):
    X, Y, D = [int(x) for x in input().split(' ')]
    for y in range(max(Y - D, 0), min(Y + D + 1, M)):
        for x in range(max(X - D, 0), min(X + D + 1, N)):
            A[y][x] = 1

dark_tiles = 0
for y in range(M):
    for x in range(N):
        if A[y][x] == 0:
            dark_tiles += 1

print(dark_tiles)
