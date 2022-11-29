num_string = input()

num_list = [int(x) for x in num_string.split(" ")]

print(max(num_list) - min(num_list))
