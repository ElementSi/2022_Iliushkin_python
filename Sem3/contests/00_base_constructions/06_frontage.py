import sys
import numpy as np


def frontage_check(front):
    return False if np.amax(front) < 2 else False


def windows_check(wins_array, h, w):
    for win in wins_array:
        if (win[0] < 0) or (win[1] > w) or (win[2] < 0) or (win[3] > h):
            return True
    return False


width, height = (int(x) for x in input().split(" "))
frontage = np.zeros((height, width), int)

windows_num = int(input())
windows_array = np.empty((windows_num, 4), int)

for i in range(windows_num):
    window_str = input()
    window = np.array([int(x) for x in window_str.split(" ")])
    windows_array[i] = window

if windows_check(windows_array, height, width):
    print("broken")
    sys.exit()

for window in windows_array:
    for i in range(window[2], window[3]):
        for j in range(window[0], window[1]):
            frontage[i][j] += 1

if frontage_check(frontage):
    print("broken")

else:
    print("correct")
