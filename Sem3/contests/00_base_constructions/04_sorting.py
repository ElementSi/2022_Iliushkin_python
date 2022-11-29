import numpy as np

length = int(input())

num_list = []
for i in range(length):
    new_num = int(input())
    num_list.append(new_num)

pos_num_array = np.sort(np.array([num for num in num_list if num >= 0]))

neg_num_list = [num for num in num_list if num < 0]
neg_num_array = np.flip(np.sort(np.array([num for num in num_list if num < 0])))

num_array = np.append(pos_num_array, neg_num_array)
num_string = " ".join(str(int(num)) for num in num_array)
print(num_string)
