n = int(input())
datas = []
need_datas = []

for _ in range(n):
    datas.append([int(x) for x in input().split()])

for data in datas:
    if (data[2] >= 10 or data[0] ** 2 + data[1] ** 2 <= 10000 or datas.count(data) > 1) and [data, datas.count(
            data)] not in need_datas:
        need_datas.append([data, datas.count(data)])

need_datas = sorted(need_datas, key=lambda x: x[0][0] ** 2 + x[0][1] ** 2)
need_datas = sorted(need_datas, key=lambda x: x[1], reverse=True)
need_datas = sorted(need_datas, key=lambda x: x[0][2], reverse=True)

for data in need_datas:
    print(data[0][0], data[0][1], data[0][2])
