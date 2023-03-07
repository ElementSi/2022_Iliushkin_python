import statistics

n = int(input())
T = []
P = []
for _ in range(n):
    data = input().split()
    T.append(float(data[0]))
    if -70 <= float(data[0]) <= 80:
        P.append(float(data[1]))

print(format(statistics.mean(T), '.4f'), format(statistics.mean(P), '.4f'))
