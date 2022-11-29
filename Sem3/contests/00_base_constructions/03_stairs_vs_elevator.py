data_string = input()

data_list = [float(x) for x in data_string.split(" ")]

stairs_time = abs(data_list[0] - data_list[1]) * data_list[5]
elevator_time = (abs(data_list[0] - data_list[1]) + abs(data_list[0] - data_list[2])) * data_list[3] + data_list[4] * 3

print("stairs" if stairs_time < elevator_time else "elevator")
