class Poke:
    def __init__(self, n, c, s):
        self.name = n
        self.classes = c
        self.strength = s


pokes = []
for line in open(input(), "r"):
    name, classes, strength = line.split(' ')
    pokes.append(Poke(name, classes.split(','), int(strength)))

target_class, target_strength = input().split()
target_strength = int(target_strength)

elite_pokes = []
for poke in pokes:
    if (target_class in poke.classes) and (poke.strength >= target_strength):
        elite_pokes.append(poke)

elite_pokes.sort(key=lambda x: x.strength, reverse=True)

for poke in elite_pokes:
    print(poke.name)
