row = input()
res_max = 0
res = 0
i = 0
while i < len(row):
    if row[i] == '1':
        res += 1
    else:
        if res > res_max:
            res_max = res
        res = 0
    i += 1
    if i == len(row) and res > res_max:
        res_max = res
print(res_max)
