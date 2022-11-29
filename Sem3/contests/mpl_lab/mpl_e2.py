import numpy as np
import matplotlib.pyplot as plt
import math as math


def vis_data(file_id, x_min=0, x_max=16, y_min=-12, y_max=12, x_tick=2, y_tick=2):
    with open("frames.txt") as f:
        lines = f.readlines()

    points_x = [float(x) for x in lines[file_id * 2].split(' ')]
    points_y = [float(x) for x in lines[file_id * 2 + 1].split(' ')]

    plt.figure(figsize=(10, 10), dpi=400)
    ax = plt.axes()

    plt.xticks(np.arange(np.ceil(x_min / x_tick) * x_tick, x_max + x_tick / 20, x_tick), fontsize=16)
    plt.yticks(np.arange(np.ceil(y_min / y_tick) * y_tick, y_max + y_tick / 20, y_tick), fontsize=16)
    plt.xlim(x_min, x_max)
    plt.ylim(y_min, y_max)

    ax.grid(which="major", c="#696969", linestyle="-", linewidth=2, alpha=0.6)

    plt.plot(
        points_x,
        points_y,
        linewidth=4
    )

    plt.title(f"Frame: {file_id}", fontsize=20)
    plt.savefig(f"mpl_e2_graphs/mpl_e2_graph_{file_id}")


vis_data(0)
vis_data(1)
vis_data(2)
vis_data(3)
vis_data(4)
vis_data(5)
