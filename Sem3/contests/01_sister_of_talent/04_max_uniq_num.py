num_list = [int(x) for x in input().split(" ")]

max_num = max(num_list)

while num_list.count(max_num) > 1:
    while num_list.count(max_num) > 0:
        num_list.remove(max_num)

    max_num = max(num_list)

print(max_num)
