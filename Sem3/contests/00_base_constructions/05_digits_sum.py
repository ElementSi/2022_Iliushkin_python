import numpy as np


def count_digit_sum(num: str):
    digits_array = np.array(list(num))
    digits_array = [int(x) for x in digits_array]
    return str(np.sum(digits_array))


number = input()

while len(number) > 1:
    number = count_digit_sum(number)

print(number)
