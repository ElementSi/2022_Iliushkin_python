import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("signals/signal03.dat", dtype=float)
plt.plot(range(1, 101), data, label="До")
data = np.insert(data, 0, np.zeros(9, ))
for i in range(9, np.size(data)):
    data[i] = np.mean(data[i - 9:i + 1])
data = data[9:]
plt.plot(range(1, 101), data, label="после")
plt.title("До и после фильтрации")
plt.legend()
plt.savefig("new3")
