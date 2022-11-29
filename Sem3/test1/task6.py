import statistics as stat

N = int(input())

sensor_data = {}

for i in range(N):
    input_line = input().split(' ')
    if input_line[0] in sensor_data:
        sensor_data[input_line[0]].append(int(input_line[1]))
    else:
        sensor_data[input_line[0]] = [int(input_line[1])]

M = int(input())

med_values = []

for i in range(M):
    input_line = input()
    try:
        med_values.append(stat.median_low(sensor_data[input_line]))

    except:
        med_values.append("no data")

for i in range(M):
    print(med_values[i])
