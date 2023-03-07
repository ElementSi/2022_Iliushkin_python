n = input()
try:
    dot = n.index(".")
except ValueError:
    n = int(n)
    print(n - 1)
else:
    length = len(n)
    accuracy = length - dot - 1
    n = float(n)
    ans = str(round(n - 1 / 10 ** accuracy, accuracy))[:length + 1]
    new_dot = ans.index(".")
    while len(ans) - new_dot - 1 < length - dot - 1:
        ans += "0"
    print(ans)
