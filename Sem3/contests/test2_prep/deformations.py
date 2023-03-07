import numpy as np

lines = list(open(input(), "r"))

N = int(lines[0].replace('\n', ''))

K = np.empty([2 * N, 2 * N])

for i in range(1, 2 * N + 1):
    line = lines[i].translate({ord('\n'): None}).split(' ')

    while '' in line:
        line.remove('')

    K[i - 1] = [float(x) for x in line]

last_line = lines[-1].translate({ord('\n'): None}).split(' ')

while '' in last_line:
    last_line.remove('')

f = np.array([float(x) for x in last_line])

K_inv = np.linalg.inv(K)

a = K_inv @ f

x_dis = []

for i in range(0, 2 * N, 2):
    x_dis.append(a[i])

x_min = min(x_dis)

print(f"{abs(x_min):.4f}" if x_min < 0 else f"{0:.4f}")
