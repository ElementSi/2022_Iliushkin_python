num_of_rows = int(input())
rows = []
checked_words = []
checked_words_lower = []
res = []

for _ in range(num_of_rows):
    rows.append(input().split())

for row in rows:
    for word in row:
        if word.lower() not in checked_words_lower:
            checked_words_lower.append(word.lower())
            checked_words.append([word])
        for word_list in checked_words:
            if word not in word_list and word.lower() in [smth.lower() for smth in word_list]:
                word_list.append(word)

for word_list in checked_words:
    if len(word_list) > 2:
        res.append([len(word_list), word_list[0].lower()])

res = sorted(res, key=lambda x: x[0], reverse=True)

for word in res:
    print(word[1])
