import matplotlib.pyplot as plt
import matplotlib.animation as an
import numpy as np

file = open("data3", 'r')
strfile = file.read().split()
str_data = np.array(strfile)
data_u = np.array([float(str_data[i]) for i in range(str_data.shape[0])])

array_u = [data_u]

time = np.arange(data_u.size)

A = np.eye(time.size) - np.roll(np.eye(time.size), -1, axis=1)

for i in range(255):
    array_u.append(array_u[i - 1] - (0.5 * A @ array_u[i - 1]))

fig = plt.figure()
ax = plt.axes(xlim=(0, 50), ylim=(0, data_u.max()))
line, = ax.plot([], [])


def init():
    line.set_data(time, array_u[0])
    return line,


def animate(i):
    line.set_data(time, array_u[i])
    return line,


animation_u = an.FuncAnimation(fig, animate, init_func=init, frames=255, interval=20, blit=True)

animation_u.save('animation.gif')
