import numpy as np
import matplotlib.pyplot as plt
import math as math


def vis_data(file_id, x_tick, y_tick):
    with open(f"dead_moroz/00{file_id}.dat") as f:
        lines = f.readlines()

    num_of_points = int(lines[0])
    points = []
    for i in range(1, num_of_points + 1):
        points.append(lines[i].split(' '))

    points_x = [float(x[0]) for x in points]
    points_y = [float(x[1]) for x in points]

    x_min = min(points_x)
    x_max = max(points_x)
    y_min = min(points_y)
    y_max = max(points_y)
    plt.xticks(np.arange(np.ceil(x_min / x_tick) * x_tick, x_max + x_tick / 20, x_tick), fontsize=16)
    plt.yticks(np.arange(np.ceil(y_min / y_tick) * y_tick, y_max + y_tick / 20, y_tick), fontsize=16)
    plt.xlim(x_min, x_max)
    plt.ylim(y_min, y_max)

    plt.figure(figsize=(16, 18 * ((y_max - y_min) / (x_max - x_min))), dpi=400)

    plt.plot(
        points_x,
        points_y,
        marker='h',
        markersize=12,
        linewidth=0
    )

    plt.title(f"Number of points: {len(points)}", fontsize=16)
    plt.savefig(f"mpl_e1_graphs/mpl_e1_graph_{file_id}")


vis_data(1, 100, 5)
vis_data(2, 100, 5)
vis_data(3, 100, 5)
vis_data(4, 100, 5)
vis_data(5, 100, 5)
