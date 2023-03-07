from math import exp


def S(s_level, t_level):
    x = (s_level - t_level) / 10
    return 1 / (1 + exp(-x))


students = list(map(int, input().split()))
N = len(students)
tasks = list(map(int, input().split()))
K = len(tasks)
target = 0.5 * K

counter = 0
for i in range(N):
    summa = 0
    for j in range(K):
        summa += S(students[i], tasks[j])
    if summa >= target:
        counter += 1

print(counter)
