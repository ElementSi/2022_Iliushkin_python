import numpy as np

lines_img = list(open(input(), "r"))
lines_my_filter = list(open(input(), "r"))

input_str = input()

P = float(input_str.split()[0])
N = int(input_str.split()[1])

len_img = len(lines_img)

img = np.empty((len_img, len_img))

for i in range(len_img):
    img[i] = [float(x) for x in lines_img[i].split()]

my_filter = np.empty((len_img, len_img))

for i in range(len_img):
    my_filter[i] = [float(x) for x in lines_my_filter[i].split()]

for i in range(N):
    img = my_filter @ img
    print(np.count_nonzero(abs(img) > P))
