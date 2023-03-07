from PIL import Image
import numpy as np

file_path = input()

img = Image.open(file_path)
data_rgb = np.array(img)

data_bw = np.floor(data_rgb[:, :, 0] * 0.299 + data_rgb[:, :, 1] * 0.587 + data_rgb[:, :, 2] * 0.114)

print(int(np.amin(data_bw)), end=' ')
print(int(np.amax(data_bw)))
