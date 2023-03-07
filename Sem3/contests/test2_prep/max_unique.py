import numpy as np

array = np.array(input().split(), int)
array_un, counts = np.unique(array, return_counts=True)
array = np.stack((array_un, counts), axis=-1)
array = np.array(array[array[:, 1] == 1])

print(array.max(axis=0)[0])
