small_letters = 'abcdefghijklmnopqrstuvwxyz'
big_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def rot13(letter):
    if letter.isupper():
        number = big_letters.index(letter)
        number = (number + 13) % 26
        letter = big_letters[number]
    else:
        number = small_letters.index(letter)
        number = (number + 13) % 26
        letter = small_letters[number]
    return letter


data = []
res = []
try:
    with open(input(), 'r') as f:
        data = f.read()
except FileNotFoundError:
    res = "Can not read file"
else:
    for char in data:
        if char in small_letters or char in big_letters:
            res.append(rot13(char))
        else:
            res.append(char)
print(''.join(res))
