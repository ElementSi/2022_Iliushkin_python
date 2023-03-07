def count_neighbours(f, height, width, x, y):
    neigh = 0
    for k in range(max(0, y - 1), min(height, y + 2)):
        for g in range(max(0, x - 1), min(width, x + 2)):
            if f[k][g] == '#' and (not (k == y and g == x)):
                neigh += 1

    return neigh


N, M, K = (int(x) for x in input().split(' '))

fields = [[], []]

for i in range(N):
    inline = input()
    fields[0].append(inline)
    fields[1].append(inline)

for i in range(K):
    for n in range(N):
        new_line = ''
        for m in range(M):
            if i % 2 == 0:
                neighbours = count_neighbours(fields[0], N, M, m, n)

                if fields[0][n][m] == '.':
                    if neighbours == 3:
                        new_line = new_line + '#'
                    else:
                        new_line = new_line + '.'

                elif fields[0][n][m] == '#':
                    if neighbours == 2 or neighbours == 3:
                        new_line = new_line + '#'
                    else:
                        new_line = new_line + '.'

            else:
                neighbours = count_neighbours(fields[1], N, M, m, n)

                if fields[1][n][m] == '.':
                    if neighbours == 3:
                        new_line = new_line + '#'
                    else:
                        new_line = new_line + '.'

                elif fields[1][n][m] == '#':
                    if neighbours == 2 or neighbours == 3:
                        new_line = new_line + '#'
                    else:
                        new_line = new_line + '.'

        if i % 2 == 0:
            fields[1][n] = new_line

        else:
            fields[0][n] = new_line

if K % 2 == 1:
    field = fields[1]

else:
    field = fields[0]

for line in field:
    print(line)
