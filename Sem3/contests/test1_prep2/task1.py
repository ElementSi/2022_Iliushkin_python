n = int(input())
datas = []

for _ in range(n):
    smth = input().split()
    datas.append([int(smth[0]), int(smth[1])])

datas = sorted(datas, key=lambda t: t[1], reverse=True)
for data in datas:
    print(data[0])
