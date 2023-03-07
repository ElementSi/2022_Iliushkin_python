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

x_tick = 5000
x_min = 0
x_max = 40000
y_min = 10**(-16)
y_max = 10**6

plt.figure(figsize=(16, 10), dpi=400)
ax = plt.axes()

algorithms = ["Jacoby", "Gauss-Seidel", "Simple"]

for i in range(3):
    with open(f"data/data_task4_{algorithms[i]}.txt") as f:
        lines = f.readlines()

    residual_array = np.array([float(x) for x in lines[:len(lines) - 1]])
    iterations_array = np.arange(0, 49999, 1)

    line_style = "-"

    if algorithms[i] == "Gauss-Seidel":
        line_style = "--"

    plt.plot(iterations_array,
             residual_array,
             c=COLORS[i - 1], linestyle=line_style, linewidth=4,
             label=f"{algorithms[i]} Iteration")

plt.xlim(x_min, x_max)
plt.xticks(np.arange(0, x_max + x_tick / 20, x_tick), fontsize=20)
ax.xaxis.set_minor_locator(plt.MultipleLocator(x_tick / 5))

ax.set_yscale('log')
ax.set_ylim(y_min, y_max)
plt.yticks(fontsize=20)
ax.yaxis.set_major_locator(tick.LogLocator(base=10**2, numticks=7))
ax.yaxis.set_minor_locator(tick.LogLocator(base=10**4, subs=(0.001, 0.01, 0.1)))
ax.yaxis.set_minor_formatter(tick.NullFormatter())

ax.grid(which="major", c="#696969", linestyle="-", linewidth=2, alpha=0.6)
ax.grid(which="minor", c="#696969", linestyle="--", linewidth=1, alpha=0.6)

plt.legend(fontsize=18)
plt.xlabel("Число итераций $n$", fontsize=24)
plt.ylabel("Евклидова норма невязки $r_2$", fontsize=24)
plt.savefig("graphs/graph_task4.png")
