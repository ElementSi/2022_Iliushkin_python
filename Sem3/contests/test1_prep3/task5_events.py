f_line = input()
D, N = [float(f_line.split(' ')[0]), int(f_line.split(' ')[1])]

data = [float(x) for x in input().split()]

events = 0
is_active = False
prev_is_active = False
for i in range(N - 1, len(data)):
    excess_num = 0
    for j in range(N):
        if abs(data[i - j]) > D:
            excess_num += 1

    if excess_num == N:
        is_active = True

    lack_num = 0

    for j in range(N):
        if abs(data[i - j]) < D:
            lack_num += 1

    if lack_num == N:
        is_active = False

    if is_active and (not prev_is_active):
        events += 1

    prev_is_active = is_active

print(events)
