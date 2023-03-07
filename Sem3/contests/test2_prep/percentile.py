from math import ceil

data = sorted([int(i) for i in input().split()])
p = int(input())
N = len(data)

print(data[ceil(N * p / 100) - 1])
