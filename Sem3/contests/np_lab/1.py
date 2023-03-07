from PIL import Image
import numpy as np

img = Image.open("lunar_images/lunar03_raw.jpg")
data = np.array(img, dtype=int)
print(data.max())
print(data)
data = data - np.full(np.shape(data), data.max())
data = data / (-data.min()) * 255 + np.full(np.shape(data), 255)
print(data)
print(data.min())
print(data.max())
res_img = Image.fromarray(data)
res_img = res_img.convert("L")
res_img.save("res3.jpg")
