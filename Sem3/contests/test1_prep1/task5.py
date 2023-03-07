try:
    with open(input(), 'r') as f:
        data = f.readlines()
except:
    print(0)
else:
    key_word = input().lower()
    res = 0

    for row in data:
        low_row = [word.lower() for word in row.split()]
        res += low_row.count(key_word)

    print(res)
