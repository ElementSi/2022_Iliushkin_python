NUM_OF_SYLONS = 3

N = int(input())

crew = dict()

for i in range(N):
    scan_data = input().split(" ")

    while '' in scan_data:
        scan_data.remove('')

    if scan_data[1] in crew:
        crew[scan_data[1]] = [min(crew[scan_data[1]][0], float(scan_data[5])),
                              max(crew[scan_data[1]][1], float(scan_data[5])),
                              crew[scan_data[1]][2] + 1]

    else:
        crew[scan_data[1]] = [float(scan_data[5]), float(scan_data[5]), 1]

crew = [(member, (data[1] - data[0])) for (member, data) in crew.items() if data[2] > 1]

to_remove = len(crew) - NUM_OF_SYLONS

for i in range(to_remove):
    m = max([x[1] for x in crew])
    crew = [x for x in crew if x[1] != m]

imposters_ids = sorted([int(x[0]) for x in crew])
imposters_ids = ' '.join(str(x) for x in imposters_ids)

if len(imposters_ids) != 0:
    print(imposters_ids)

else:
    print(-1)
