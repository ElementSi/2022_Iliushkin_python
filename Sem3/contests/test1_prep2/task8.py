n = int(input())
datas = []

for _ in range(n):
    smth = input().split()
    datas.append([int(smth[0]), smth[1], int(smth[2])])

datas = sorted(datas, key=lambda x: x[1])
datas = sorted(datas, key=lambda x: x[0])

for data in datas:
    i = datas.index(data) + 1
    while i < len(datas):
        if data[2] == datas[i][2] and data[1] == datas[i][1]:
            datas.pop(i)
        elif data[1] == datas[i][1] and data[2] != datas[i][2]:
            break
        else:
            i += 1
# for data in datas:
#     i = datas.index(data)
#     while i < len(datas) - 1:
#         while (data[1] != datas[i][1] or datas.index(data) == i) and i < len(datas) - 1:
#             i += 1
#         try:
#             if data[2] == datas[i][2]:
#                 datas.remove(datas[i])
#         except IndexError:
#             break

for data in datas:
    print(data[0], data[1], data[2])
