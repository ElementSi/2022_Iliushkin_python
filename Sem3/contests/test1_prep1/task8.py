class Something:
    def __init__(self):
        self.data = []

    def set(self, time, name, value):
        for field in reversed(self.data):
            if field[1] == name and len(field[0]) == 1:
                field[0].append(time)
        self.data.append([[time + 1], name, value])

    def delete(self, time, name):
        for field in reversed(self.data):
            if field[1] == name and len(field[0]) == 1:
                field[0].append(time)

    def show(self, time):
        res = []
        output = []
        for field in self.data:
            if len(field[0]) == 2 and field[0][0] <= time <= field[0][1]:
                res.append(field)
            elif len(field[0]) == 1 and field[0][0] <= time:
                res.append(field)
        if not res:
            print("(none)")
        else:
            res = sorted(res, key=lambda x: x[1])
            output = ", ".join(info[1] + " : " + info[2] for info in res)
            print(output)


obj = Something()

n = int(input())
for _ in range(n):
    command = input().split()
    if command[1] == "SET":
        obj.set(int(command[0]), command[2], command[3])
    else:
        obj.delete(int(command[0]), command[2])

k = int(input())
for _ in range(k):
    time = int(input())
    obj.show(time)
