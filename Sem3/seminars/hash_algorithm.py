def complement_beg(word, fin_len, sign):
    while len(word) < fin_len:
        word = sign + word
    return word


def complement_end(word, fin_len, sign):
    while len(word) < fin_len:
        word = word + sign
    return word


def grouper(iterable, n):
    args = [iter(iterable)] * n
    return zip(*args)


def right_rotate(str_0, num):
    lists = list(str_0)
    output_list = []

    for item in range(len(lists) - num, len(lists)):
        output_list.append(lists[item])

    for item in range(0, len(lists) - num):
        output_list.append(lists[item])

    return ''.join(output_list)


def right_shift(str_0, num):
    lists = list(str_0)
    output_list = []

    for item in range(len(lists) - num, len(lists)):
        output_list.append(lists[item])

    for item in range(0, len(lists) - num):
        output_list.append(lists[item])

    for i in range(num):
        output_list[i] = '0'

    return ''.join(output_list)


def xor(str_1, str_2):
    return ''.join(str(ord(a) ^ ord(b)) for a, b in zip(str_1, str_2))


def turn_into_cash(word):
    cash = ''
    for sign in word:
        cash += complement_beg(bin(ord(sign)).split('b')[1], 8, '0')

    cash += '1'

    cash = complement_end(cash, 448, '0')

    cash += complement_beg(bin(len(word) * 8).split('b')[1], 64, '0')

    cash_list = [''.join(i) for i in grouper(cash, 32)]

    cash_list += ['0' * 32 for i in range(48)]

    for i in range(16, 64):
        s0 = xor(xor(right_rotate(cash_list[i - 15], 7), right_rotate(cash_list[i - 15], 18)), right_shift(cash_list[i - 15], 3))
        s1 = xor(xor(right_rotate(cash_list[i - 2], 17), right_rotate(cash_list[i - 2], 19)), right_shift(cash_list[i - 2], 10))
        num10 = complement_beg(bin(int(cash_list[i - 16], 2) + int(s0, 2) + int(s1, 2) + int(cash_list[i - 7], 2)).split('b')[1], 32, '0')
        cash_list[i] = num10[-32:]

    return cash_list


print(turn_into_cash(input()))
