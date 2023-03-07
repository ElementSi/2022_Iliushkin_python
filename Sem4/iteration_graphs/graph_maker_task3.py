import numpy as np
import matplotlib.ticker as tick
import matplotlib.pyplot as plt


COLORS = [
    "#13EA3B",
    "#1390EA",
    "#A913EA",
    "#EA1333",
    "#EA7B13"
]

x_tick = 0.02
x_min = 0
x_max = 0.1940
y_min = 10**2
y_max = 10**5

plt.figure(figsize=(16, 10), dpi=400)
ax = plt.axes()

with open(f"data/data_task3.txt") as f:
    lines = f.readlines()

iterations_array = np.array([float(x) for x in lines[:len(lines) - 1]])
tau_array = np.arange(0.0001, 0.1940, 0.0001)

plt.plot(tau_array,
         iterations_array,
         c=COLORS[0], linewidth=4,
         label="Number of iterations n = n(τ)")

plt.xlim(x_min, x_max)
plt.xticks(np.arange(0, x_max + x_tick / 20, x_tick), fontsize=20)
ax.xaxis.set_minor_locator(plt.MultipleLocator(x_tick / 5))

ax.set_yscale('log')
ax.set_ylim(y_min, y_max)
plt.yticks(fontsize=20)
ax.yaxis.set_major_locator(tick.LogLocator(base=10, numticks=5))
ax.yaxis.set_minor_locator(tick.LogLocator(base=10, subs=np.arange(1.0, 10.0)))
ax.yaxis.set_minor_formatter(tick.NullFormatter())

ax.grid(which="major", c="#696969", linestyle="-", linewidth=2, alpha=0.6)
ax.grid(which="minor", c="#696969", linestyle="--", linewidth=1, alpha=0.6)

plt.legend(fontsize=18)
plt.xlabel("Шаг итерации $τ$", fontsize=24)
plt.ylabel("Число итераций $n$", fontsize=24)
plt.savefig("graphs/graph_task3.png")