word_list = input().split(" ")
word_list = list({(w, word_list.count(w)) for w in word_list})
word_list.sort(key=lambda w: (w[0], -w[1]))
for word in word_list: print(f"{word[1]} {word[0]}")
