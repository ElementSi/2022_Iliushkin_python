try:
    cats = []
    for line in open(input(), "r"):
        cats.append([line.split()[0], float(line.split()[1])])
    cats.sort(key=lambda x: x[1], reverse=True)

    N = int(input())
    for i in range(N):
        print(cats[i][0])

except:
    print("Can not read data")
