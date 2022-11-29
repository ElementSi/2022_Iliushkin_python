word_set = set(input().split(" "))
word_list = list(word_set)
word_list.sort(key=lambda w: w[0])
word_list.sort(reverse=True, key=len)

for word in word_list:
    print(word)
