import scipy as sp
import numpy as np
import matplotlib.pyplot as plt

sys_name = input()

input_file = sys_name + '.txt'

lines = list(open(input_file, "r"))

N = int(lines[0].replace('\n', ''))

A = np.empty([N, N])

for i in range(1, N + 1):
    line = lines[i].translate({ord('\n'): None}).split(' ')

    while '' in line:
        line.remove('')

    A[i - 1] = [float(x) for x in line]

b = np.array([float(x) for x in lines[-1].translate({ord('\n'): None}).split(' ')])

print(A)
print(b)

x = sp.linalg.solve(A, b)

fig, ax = plt.subplots(1, 1)
fig.set_size_inches(10, 6)
plt.subplots_adjust(left=0.1,
                    bottom=0.1,
                    right=0.95,
                    top=0.9)

ax.bar(np.arange(1, x.size + 1), x, color='#1047CF', width=0.5)

ax.set_title('Solutions')
ax.grid(which="major", c="#696969", linestyle="-", linewidth=1, alpha=0.6)

plt.savefig(f'{sys_name}_solution.png', dpi=400)
