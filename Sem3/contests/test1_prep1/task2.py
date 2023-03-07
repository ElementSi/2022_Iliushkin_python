row = input().split()
res = 0
for smth in row:
    try:
        int(smth)
    except:
        pass
    else:
        res += int(smth)
print(res)
