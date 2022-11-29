def nonacci_of(n):
    n_p = [0, 0, 0, 0, 0, 0, 0, 0, 1]
    for i in range(n - 9):
        n_p = [n_p[1], n_p[2], n_p[3], n_p[4], n_p[5], n_p[6], n_p[7], n_p[8],
               n_p[0] + n_p[1] + n_p[2] + n_p[3] + n_p[4] + n_p[5] + n_p[6] + n_p[7] + n_p[8]]
    return n_p[8] if n > 8 else n_p[0]


print(nonacci_of(int(input())))
