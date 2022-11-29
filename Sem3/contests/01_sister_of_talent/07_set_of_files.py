address_list = input().split(' ')
word_set = set()

for address in address_list:
    try:
        word_set = word_set | {word for line in open(address, "r") for word in line.split()}
    except:
        pass

for word in sorted(list(word_set)): print(word, end=' ')
